from Modulos.Modulo_Language import (
    get_text as Lang,
    Default_Language
)
from Modulos.Modulo_GT import Translate

import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class Window_Main(Gtk.Window):
    def __init__(self):
        super().__init__( title=Lang("trs") )
        self.set_resizable(True)
        self.set_default_size(308, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8
        )
        
        # Secciones Vertical - Opciones
        self.button_set_file = Gtk.Button( label=Lang('set_arch') )
        self.button_set_file.connect('clicked', self.evt_set_file)
        vbox_main.pack_start(self.button_set_file, True, False, 0)
        
        self.button_set_text = Gtk.Button( label=Lang('set_txt') )
        self.button_set_text.connect('clicked', self.evt_set_text)
        vbox_main.pack_start(self.button_set_text, True, False, 0)
        
        # Fin - Agregar contenedor principal
        self.add(vbox_main)
    
    def evt_set_file(self, widget):
        self.hide()
        dialog = Dialog_translator_file(self)
        dialog.run()
        dialog.destroy()
        self.show_all()

    def evt_set_text(self, widget):
        self.hide()
        dialog = Dialog_translator_txt(self)
        dialog.run()
        dialog.destroy()
        self.show_all()


class Dialog_translator_file(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(
            title=Lang('trs_file'),
            transient_for=parent, flags=0
        )
        self.set_resizable(True)
        self.set_default_size(512, -1)
        
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
        
        # Sección Vertical - Establecer Language input y output
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label = Gtk.Label(label=f'{Lang("lang")}: ')
        hbox.pack_start(label, False, True, 8)
        
        self.entry_i_lang = Gtk.Entry(
            text=str(Default_Language()),
            placeholder_text=Lang('i')
        )
        hbox.pack_start(self.entry_i_lang, False, True, 0)
        
        self.entry_o_lang = Gtk.Entry(
            text='',
            placeholder_text=Lang('o')
        )
        hbox.pack_end(self.entry_o_lang, False, True, 0)
        
        # Seccion vertical - Iniciar traducción
        button_start_translate = Gtk.Button(
            label = Lang('start')
        )
        vbox_main.pack_start(button_start_translate, True, False, 8)
        
        # Fin - Establecer todo
        self.get_content_area().add(vbox_main)
        self.show_all()
    
    def evt_set_input_dir(self, widget):
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
        elif response == Gtk.ResponseType.CANCEL:
            pass
        
        dialog.destroy()


class Dialog_translator_txt(Gtk.Dialog):
    def __init__(self, parent):
        super().__init__(
            title=Lang('trs_txt'),
            transient_for=parent, flags=0
        )
        self.set_resizable(True)
        self.set_default_size(308, -1)
        
        # Contenedor Principal
        vbox_main = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        vbox_main.set_property('expand', True)
        
        # Sección Vertical - Establecer Language input y output
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=4)
        vbox_main.pack_start(hbox, True, False, 0)
        
        label = Gtk.Label(label=f'{Lang("lang")}: ')
        hbox.pack_start(label, False, True, 8)
        
        self.entry_i_lang = Gtk.Entry(
            text=str(Default_Language()),
            placeholder_text=Lang('i')
        )
        hbox.pack_start(self.entry_i_lang, True, True, 0)
        
        self.entry_o_lang = Gtk.Entry(
            text='',
            placeholder_text=Lang('o')
        )
        hbox.pack_start(self.entry_o_lang, True, True, 0)
        
        # Seccion vertical - Iniciar traducción
        button_start_translate = Gtk.Button(
            label = Lang('start')
        )
        vbox_main.pack_start(button_start_translate, True, False, 8)
        
        # Fin - Establecer todo
        self.get_content_area().add(vbox_main)
        self.show_all()


win = Window_Main()
win.connect('destroy', Gtk.main_quit)
win.show_all()
Gtk.main()