from os.path import isfile
from Modulos.Modulo_GT import Translate, list_lang
import threading
from Modulos.Modulo_Text import (
    Text_Read
)
from Modulos.Modulo_Language import (
    get_text as Lang,
    Default_Language
)
from Interface import Modulo_Util_Gtk as Util_Gtk

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib


class Window_Main(Gtk.Window):
    def __init__(self):
        super().__init__( title=f"{Lang('trs')} - @CocoMarck GitHub" )
        self.set_resizable(True)
        self.set_default_size(308, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        vbox_main.set_property('expand', True)
        
        # Sección Vertical - Establecer archivo de texto
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        vbox_main.pack_start(hbox, True, False, 0)

        self.entry_i_dir = Gtk.Entry(
            placeholder_text=Lang('arch')
        )
        hbox.pack_start(self.entry_i_dir, True, True, 0)
        
        button_i_dir = Gtk.Button( label=Lang('set_arch') )
        button_i_dir.connect('clicked', self.evt_set_input_dir)
        hbox.pack_end(button_i_dir, False, True, 0 )
        
        # Sección vertical - Texto en un Text View
        scroll_win = Gtk.ScrolledWindow(
            hexpand=True,
            vexpand=True
        )
        vbox_main.pack_start(scroll_win, True, True, 0)
        
        self.text_view = Gtk.TextView(
            editable=True
        )
        scroll_win.add( self.text_view )
        
        # Sección Vertical - Establecer Language input y output
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label = Gtk.Label(label=f'{Lang("lang")}: ')
        hbox.pack_start(label, False, True, 8)
        
        self.entry_i_lang = Gtk.Entry(
            text=str(Default_Language()),
            placeholder_text=Lang('i')
        )
        completion = Gtk.EntryCompletion()
        completion.set_model( Gtk.ListStore(str) )
        for lang in list_lang:
            completion.get_model().append( [lang] )
        completion.set_text_column(0)
        self.entry_i_lang.set_completion(completion)
        hbox.pack_start(self.entry_i_lang, True, True, 0)
        
        self.entry_o_lang = Gtk.Entry(
            text='',
            placeholder_text=Lang('o')
        )
        completion = Gtk.EntryCompletion()
        completion.set_model( Gtk.ListStore(str) )
        for lang in list_lang:
            completion.get_model().append( [lang] )
        completion.set_text_column(0)
        self.entry_o_lang.set_completion(completion)
        hbox.pack_start(self.entry_o_lang, True, True, 0)
        
        # Seccion vertical - Iniciar traducción
        button_start_translate = Gtk.Button(
            label = Lang('start')
        )
        button_start_translate.connect('clicked', self.evt_start_translate)
        vbox_main.pack_start(button_start_translate, True, False, 8)
        
        # Fin - Agregar contenedor principal
        self.add(vbox_main)
    
    def evt_set_input_dir(self, widget):
        # Establecer un archivo de texto, y si se logra detectar texto, establecerlo en el text view

        dialog = Gtk.FileChooserDialog(
            parent=self,
            title=Lang('set_dir'),
            action=Gtk.FileChooserAction.OPEN
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL,
            Gtk.ResponseType.CANCEL,
            Lang('set'),
            Gtk.ResponseType.OK
        )
        dialog.set_current_folder( self.entry_i_dir.get_text() )

        filter_txt = Gtk.FileFilter()
        filter_txt.set_name( Lang('text') )
        filter_txt.add_mime_type('text/plain')
        dialog.add_filter(filter_txt)
        
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            self.entry_i_dir.set_text( dialog.get_filename() )
            if isfile(dialog.get_filename()):
                text = Text_Read(
                    file_and_path=dialog.get_filename(),
                    option='ModeText'
                )
                self.text_view.get_buffer().set_text(text)
            
        elif response == Gtk.ResponseType.CANCEL:
            pass
        
        dialog.destroy()
    
    def evt_start_translate(self, widget):
        # Verificar que los parametros esten correctos
        text_error = ''
        
        buffer_text_view = self.text_view.get_buffer()
        self.text_input = buffer_text_view.get_text(
            buffer_text_view.get_start_iter(),
            buffer_text_view.get_end_iter(),
            False
        )
        if self.text_input == '':
            text_error += f'ERROR - {Lang("text")}\n'
        
        if self.entry_i_lang.get_text() == '':
            text_error += f'ERROR - {Lang("lang")} | {Lang("i")}\n'
            
        if self.entry_o_lang.get_text() == '':
            text_error += f'ERROR - {Lang("lang")} | {Lang("o")}\n'
        
        
        # Fin - Traducir o no
        if text_error == '':
            # Preguntar si guardar traduccion o no.
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.QUESTION,
                buttons=Gtk.ButtonsType.YES_NO,
                text=Lang('save-or-no_trs')
            )
            response = dialog.run()

            # Traducir mediante un hilo
            if response == Gtk.ResponseType.YES:
                dialog.destroy()

                dialog = Gtk.FileChooserDialog(
                    title=Lang('save_arch'), parent=self,
                    action=Gtk.FileChooserAction.SAVE
                )
                dialog.add_buttons(
                    Gtk.STOCK_CANCEL,
                    Gtk.ResponseType.CANCEL,
                    Gtk.STOCK_SAVE,
                    Gtk.ResponseType.OK
                )
                dialog.set_current_name( f"{Lang('name')}.txt" )

                filter_txt = Gtk.FileFilter()
                filter_txt.set_name( Lang('text') )
                filter_txt.add_mime_type('text/plain')
                dialog.add_filter(filter_txt)
                
                response = dialog.run()
                if response == Gtk.ResponseType.OK:
                    self.text_output = dialog.get_filename()

                    self.dialog_wait = Util_Gtk.Dialog_Wait(
                        self, text=Lang('wait')
                    )

                    self.save_translate = True
                    self.thread = threading.Thread(
                        target=self.thread_translate
                    )
                    self.thread.start()
                    
                    self.dialog_wait.run()
                    
                elif response == Gtk.ResponseType.CANCEL:
                    pass
                
                dialog.destroy()

            elif response == Gtk.ResponseType.NO:
                dialog.destroy()

                self.text_output = self.text_input

                self.dialog_wait = Util_Gtk.Dialog_Wait(
                    self, text=Lang('wait')
                )

                self.save_translate = False
                self.thread = threading.Thread(
                    target=self.thread_translate
                )
                self.thread.start()
                
                self.dialog_wait.run()
            
            dialog.destroy()

        else:
            # Error en alguno de los parametros
            dialog = Gtk.MessageDialog(
                transient_for=self,
                flags=0,
                message_type=Gtk.MessageType.ERROR,
                buttons=Gtk.ButtonsType.OK,
                text=text_error
            )
            dialog.run()
            dialog.destroy()
    
    def thread_translate(self):
        if self.save_translate == True:
            pass
        else:
            self.text_output = None

        #print(
        #    f'{self.entry_i_lang.get_text()}\n'
        #    f'{self.entry_o_lang.get_text()}\n'
        #    f'{self.text_input}\n'
        #    f'{self.text_output}'
        #)
        self.text_translate = Translate(
            language_input = self.entry_i_lang.get_text(),
            language_output = self.entry_o_lang.get_text(),
            output_text = self.text_output,
            text_only = self.text_input,
            print_mode = False
        )
        
        GLib.idle_add(self.thread_translate_finish)
    
    def thread_translate_finish(self):
        self.dialog_wait.destroy()
        
        # Si la traducción falla, se mostrara remplazara la variable que contendira la traducción, por un mensaje de error
        if self.text_translate == None:
            self.text_translate = f"ERROR - {Lang('error_parameter')}"
        else:
            pass
        
        # Fin - Mostrar texto traducido
        dialog = Util_Gtk.Dialog_TextView(
            self,
            text=self.text_translate
        )
        dialog.run()
        dialog.destroy()


win = Window_Main()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()