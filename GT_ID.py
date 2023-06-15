from Modulo_GT import (
    input_text,
    id_number,
    id_input,
    id_output,
    text_only,
    language_input,
    language_output,
    output_text
)
from Modulo_Util import (
    Text_Read,
    Path,
)
from Modulo_ShowPrint import (
    Title,
    Separator
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
        #print('ERROR - Lenguage input or output, no detects')

    
    # Verificar que este listo el objeto para traducir texto
    if translator == None:
        # Si el translator no esta correcto.
        print(
            'ERROR - Parameters, not goods'
        )
    else:
        # Empezar a traducir
        if type( input_text() ) is str:
            # Si el input_text es un archivo de texto
            try:
                # Traducir input_text
                to_translate = Text_Read(
                    file_and_path=input_text(),
                    opc='ModeText'
                )
            except:
                # El input no es un texto.
                to_translate = None
                if os.path.isdir( input_text() ):
                    # El input es un directorio
                    try:
                        # Traducir id
                        to_translate = Text_Read(
                            file_and_path=(
                                Path(input_text()) +
                                id_input()
                            ),
                            opc='ModeText'
                        )
                    except:
                        # No traducir
                        pass
                else:
                    # No traducir
                    pass

        else:
            to_translate = None
            
            try:
                # ID Traducir
                to_translate = Text_Read(
                    file_and_path=id_input(),
                    opc='ModeText'
                )
            except:
                # ID No traducir
                pass
            
            if type( text_only() ) is str:
                # --text_only, Traducrir un str
                to_translate = text_only()
        

        # Ralizar eventos, de imprimir y/o guardar archivos
        if type( to_translate ) is str:
            translate_ready = translator.translate( to_translate )

            Title(text=language_input())
            print(to_translate)
            Separator()
            Title(text=language_output())
            print(translate_ready)
            
            try:
                if type( output_ready ) is str:
                    if os.path.isdir( output_ready ):
                        # Para el ID, Modo ID y dir
                        output_text = Path(output_ready) + id_output()

                    else:
                        # Traduccion Modo Normal
                        output_text = output_ready

                else:
                    # Para el ID, Modo ID sin dir
                    if type( id_number() ) is str:
                        output_text = id_output()
                    else:
                        output_text = None

                if type (output_text) is str:
                    # Meter traduccion al output
                    with open(output_text, 'w') as text_output:
                        text_output.write(translate_ready)

                    Separator()
                    print('Text Saved')
                else:
                    pass

            except:
                Separator()
                print('ERROR - Output, not good')

        else:
            Separator()
            print('ERROR - Translating')


if __name__ == '__main__':
    # Variable necesaria, o si no, el valor siempre sera None
    output_ready = output_text()
    
    # Iniciar proceso
    Translate()