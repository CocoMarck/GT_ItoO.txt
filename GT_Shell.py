from Modulos.Modulo_GT import Translate, list_lang
from Modulos.Modulo_System import CleanScreen
from Modulos.Modulo_ShowPrint import (
    Title,
    Continue,
    Separator
)
from Modulos.Modulo_Language import (
    get_text as Lang,
    Default_Language,
    YesNo
)


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
            if option in dict_options.keys():
                go = Continue()
                if go == YesNo('yes'):
                    go = True
                else:
                    go = False

            else:
                go = False
            
            if not go == True:
                option = None
            
            # En base a la opcion elegida, iniciar eventos...
            if option == '1':
                self.start_translator()

            elif option == '0':
                loop = False

            elif option == None:
                pass

            else:
                input(f'ERROR - {Lang("see_options")}')
    
    def start_translator(self):
        CleanScreen()
        Title( Lang('text') )
        Continue( Lang('set_arch') )



if __name__ == '__main__':
    Translator()