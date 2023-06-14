import argparse
from deep_translator import GoogleTranslator
from pathlib import Path as pathlib
from Modulo_Util import (
    Text_Read,
    CleanScreen,
    Title,
    Separator
)


# Objeto para los parametros
parser = argparse.ArgumentParser()

# Parametro - File
parser.add_argument(
    '-i',
    '--input_text',
    help='Text file - Essential'
)

# Parametro - Text Only
parser.add_argument(
    '-t',
    '--text_only',
    help='String text'
)

# Parametro - ID
parser.add_argument(
    '-id',
    '--id_number',
    help='ID essential.'
)

# Parametro - Languaje de entrada
parser.add_argument(
    '-langI',
    '--language_input',
    help='Language import input'
)

# Parametro - Languaje de salida
parser.add_argument(
    '-langO',
    '--language_output',
    help='Language export output'
)

# Parametro - File output
parser.add_argument(
    '-o',
    '--output_text',
    help='Output for save the file.txt'
)

# Argumentos listos, para hacer lo chido
args = parser.parse_args()

# Evento - Parametro file
def input_text():
    try:
        if pathlib(args.input_text).exists():
            return args.input_text
        else:
            print('ERROR - This is not a file')
    except:
        pass

# Evento - Parametro texto only
def text_only():
    try:
        return args.text_only
    except:
        print('ERROR - Text not found')

# Evento - Parametro id number
def id_number():
    try:
        if (
            type( float(args.id_number) ) is float
        ):
            # Si id_numeber no es flotante
            return args.id_number
        else:
            # Si id_number no es un numero flotante
            print('ERROR - The id is not float')
    except:
        print('ERROR - The id is not float')
    
# Evento - Parametro language input
def language_input():
    try:
        return args.language_input
    except:
        print('ERROR - Select a input language')

# Evento - Parametro language output
def language_output():
    try:
        return(args.language_output)
    except:
        print('ERROR - Select a output language')


# Texto a traducir
def Translate_and_save():
    # Objeto - Traductor
    if (
        language_input() == None or
        language_output() == None
    ):
        # Si no existe los languages de input o output
        print('ERROR - Languege input or output, not goods')
    else:
        translator = GoogleTranslator(
            source=language_input(),
            target=language_output()
        )


    if input_text() == None:
        # Si el archivo a traducir no existe
        if text_only() == None:
            pass
        else:
            text_translate = translator.translate( text_only() )
            print(text_translate)

    else:
        # Si existe el archivo.txt
        try:
            text_file = Text_Read(
                file_and_path=input_text(),
                opc='ModeText'
            )
        except:
            # Si no existe el archivo.txt
            print('ERROR - This is not a text file')

        try:
            # Traducir
            text_translate = translator.translate(text_file)

            # Mostrar texto original
            # Mostrar texto traducido
            print(
                Title(language_input(), see=False) +
                text_file + '\n\n' +

                Title(language_output(), see=False) +
                text_translate + '\n\n'+
                
                Separator(see=False)
            )

            try:
                with open(args.output_text, 'w') as text_output:
                    text_output.write(text_translate)
            except:
                print('WARNING - Output not good')
                
            print("Translated - That's good")

        except:
            # Si no se puede traducir
            pass


# Ejecutar programa y salir
try:
    Translate_and_save()
except:
    print('ERROR - Parameters, not goods')