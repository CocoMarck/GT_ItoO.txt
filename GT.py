from Modulo_Util import (
    CleanScreen,
    Path,
)
from Modulo_GT import (
    input_text,
    id_number,
    text_only,
    language_input,
    language_output,
    output_text
)
from deep_translator import GoogleTranslator
import os


def Translate():
    # Alistar Objeto de Traduccion
    if (
        type ( language_input() ) is str and
        type ( language_output() ) is str
    ):
        # Si los lengujes son str
        try:
            # Objeto Traducir
            translator = GoogleTranslator(
                source=language_input(),
                target=language_output()
            )
        except:
            # Parametros para objeto traducir, erroneos
            translator = None

    else:
        # Los languages, no son str, por lo tanto, no es nada
        translator = None
        print('ERROR - Lenguage input or output, no detects')

    
    # Verificar que este listo el objeto para traducir texto
    if translator == None:
        # Si el translator no esta correcto.
        print(
            'ERROR - Parameters, lang_input or lang_output'
        )
    else:
        # Empezar a traducir
        if type( input_text() ) is str:
            # Si el input_text es un archivo de texto
            try:
                to_translate = Text_Read(
                    file_and_path=input_text(),
                    opc='ModeText'
                )
            except:
                to_translate = None
                dir_ready = input_text()

        else:
            to_translate = None
            
            if type( text_only() ) is str:
                to_translate = text_only()
        
        # Ralizar eventos, de imprimir y/o guardar archivos
        if type( to_translate ) is str:
            translate_ready = translator.translate( to_translate )
            print(
                to_translate + '\n\n' +
                translate_ready
            )
            
            try:
                if type( output_text() ) is str:
                    if os.path.isdir( output_text() ):
                        # Para el ID
                        pass
                    else:
                        # Meter Traduccion al output.
                        with open(output_text(), 'w') as text_output:
                            text_output.write(translate_ready)
                    print('Text Saved')
                else:
                    pass
            except:
                print('ERROR - Output, not good')

        else:
            print('ERROR - Translating')


if __name__ == '__main__':
    Translate()