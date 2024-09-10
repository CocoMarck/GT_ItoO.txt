from logic.Modulo_GT import Translate, list_lang
from logic.Modulo_System import CleanScreen
from logic.Modulo_Text import Text_Read
from interface.Modulo_ShowPrint import (
    Title,
    Continue,
    Separator,
    Archive_Path
)
from data.Modulo_Language import (
    get_text as Lang,
    Default_Language,
    YesNo
)
import os


class Translator:
    def __init__(self):
        loop = True
        while loop == True:
            # Visual - Titulo
            CleanScreen()
            Title( f'{Lang("trs")} - @CocoMarck GitHub' )
            
            # Opciones en un diccionario
            dict_options = {
                '1': f"{Lang('start')} | {Lang('trs')}",
                '0': Lang('exit')
            }
            
            # Visual - Seleccionar una opción
            for key in dict_options.keys():
                print(f'{key}. {dict_options[key]}')
            
            option = input(f'{Lang("set_option")}: ')
            
            # Verificar que la opcion elegida exista
            # Preguntar si continuar o no
            if option in dict_options.keys():
                go = Continue()
                if go == YesNo('yes'):
                    go = True
                else:
                    option = 'NO_Continue'

            else:
                go = False
                
            
            # En base a la opcion elegida, iniciar eventos...
            if option == '1':
                self.start_translator()

            elif option == '0':
                loop = False
            
            elif option == 'NO_Continue':
                pass

            else:
                input(f'ERROR - {Lang("see_options")}')
    
    def start_translator(self):
        # Parte visual - Lenguaje de entrada y salida
        CleanScreen()
        Title(Lang('lang'))
        print( f"# {Lang('exmps')}: " )
        for lang in list_lang:
            print(f'# {lang}')
        print()
        i_lang = input(f'{Lang("i")}: ')
        o_lang = input(f'{Lang("o")}: ')  
        
        # Parte visual - Establecer erchivo de texto
        CleanScreen()
        Title( Lang('trs_txt') )
        set_arch = Continue( Lang('set_arch') )
        
        # Texto
        if set_arch == YesNo('yes'):
            # Parte visual - archivo de texto
            CleanScreen()
            Title( Lang('trs_txt') )
            text = input( f"{Lang('set_arch')}: " )
            
            # Verificar que exista el archivo
            if os.path.isfile(text):
                try:
                    text = Text_Read(
                        file_and_path=text,
                        option='ModeText'
                    )
                except:
                    text = None
            else:
                text = None
        else:
            # Parte visual - Texto
            CleanScreen()
            Title( Lang('text') )
            text = input(f'{Lang("text")}: ')    
        
        # Parte Visual - Guardar texto
        CleanScreen()
        Title( Lang('trs_file') )
        save = Continue(Lang('save-or-no_trs'))
        if save == YesNo('yes'):
            CleanScreen()
            save = Archive_Path()
            CleanScreen()
            input(
                save + '\n'
                f"{Lang('continue_enter')}..."
            )
            
        else:
            save = None
        

        # Verificar que los parametros esten bien...
        text_error = ''
        if text == None or text == '':
            text_error += f'ERROR - {Lang("text")}\n'

        if i_lang == '':
            text_error += f'ERROR - {Lang("lang")} | {Lang("i")}\n'
        
        if o_lang == '':
            text_error += f'ERROR - {Lang("lang")} | {Lang("o")}\n'

        if text_error == '':       
            # Iniciar traducción.
            try:
                text_translate = Translate(
                    language_input = i_lang,
                    language_output = o_lang,
                    output_text = save,
                    text_only = text,
                    print_mode = False
                )
            except:
                text_translate = Lang('error_parameter')
            
            CleanScreen()
            Title( Lang('trs') )
            input(
                text_translate + '\n'
                '\n'
                f"{Lang('continue_enter')}..."
            )
        else:
            CleanScreen()
            input(text_error)


if __name__ == '__main__':
    Translator()