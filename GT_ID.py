import argparse
from deep_translator import GoogleTranslator
from pathlib import Path as pathlib
from Modulo_Util import (
    Text_Read,
    CleanScreen,
    Title,
    Separator,
    Path
)


# Objeto para los parametros
parser = argparse.ArgumentParser()


# Parametro - Directorio de entrada
parser.add_argument(
    '-i',
    '--input_dir',
    help='input for id'
)

# Parametro - ID
parser.add_argument(
    '-id',
    '--id_number',
    help='ID essential.'
)

# Parametro - Text Only
parser.add_argument(
    '-t',
    '--text_only',
    help='String text'
)

# Parametro - Languaje de entrada
parser.add_argument(
    '-li',
    '--language_input',
    help='Language import input'
)

# Parametro - Languaje de salida
parser.add_argument(
    '-lo',
    '--language_output',
    help='Language export output'
)

# Parametro - Directorio de salida
parser.add_argument(
    '-o',
    '--output_dir',
    help='Output for save the id.txt'
)

# Argumentos listos, para hacer lo chido
args = parser.parse_args()


# Evento - Directorio de entrada
def input_dir():
    try:
        if pathlib(args.input_dir).exists():
            return args.input_dir
        else:
            print('ERROR - Input not good')
    except:
        pass


# Evento - Parametro file
def id_number():
    try:
        # Verificar que sea un numero
        if float(args.id_number):
            pass

        # Alistar id_li.txt
        return f'{args.id_number}_{args.language_input}.txt'

    except:
        print('ERROR - This is not a number')


# Texto a traducir
def Translate_and_save():
    # Objeto - Traductor
    if (
        args.language_input == None or
        args.language_output == None
    ):
        # Si no existe los languages de input o output
        print('ERROR - Languege input or output, not founds')
        lang_not_good = True
    else:
        try:
            # Si puede traducir
            translator = GoogleTranslator(
                source=args.language_input,
                target=args.language_output
            )
            lang_not_good = False

        except:
            # Si no puede traducir
            lang_not_good = True
            print('ERROR - Languege input or output, not goods')


    # ID number
    if (
        id_number() == None or
        lang_not_good == True
    ):
        # Si el id no se asigna, o no hay languages
        if args.text_only == None:
            # Si el modo solo texto no existe
            pass
        else:
            # Si existe el modo solo texto
            text_translate = translator.translate( args.text_only )
            print(text_translate)

    else:
        # Si se asigna el id
        # Leer el archivo de texto.
        if input_dir() == None:
            text_file = Text_Read(
                file_and_path=id_number(),
                opc='ModeText'
            )
        else:
            text_file = Text_Read(
                file_and_path=(
                    Path( input_dir() ) +
                    id_number()
                ),
                opc='ModeText'
            )

        try:
            # Traducir
            text_translate = translator.translate(text_file)

            # Mostrar texto original
            # Mostrar texto traducido
            print(
                Title(args.language_input, see=False) +
                text_file + '\n\n' +

                Title(args.language_output, see=False) +
                text_translate + '\n\n'+
                
                Separator(see=False)
            )

            # Output
            if args.output_dir == None:
                output_dir = './'
            else:
                output_dir = Path(args.output_dir)

            # Meter lo traducido en un archivo de texto.
            try:
                # Intentar escribir traducción en el output
                with open(
                    output_dir +
                    f'{args.id_number}_{args.language_output}.txt',
                    'w'
                ) as text_output:
                    text_output.write(text_translate)
            except:
                # Si no se puede escribir el texto.
                print('ERROR - Output not good')
                
            # Indicador, que se tradujo correctamente
            print("Translated - That's good")

        except:
            # Si no se puede traducir
            pass


# Ejecutar programa y salir
try:
    Translate_and_save()
except:
    print('ERROR - Parameters, not goods')