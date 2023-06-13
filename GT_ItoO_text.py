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

# Parametro - ID
parser.add_argument(
    '-id',
    '--id_number',
    help='ID essential.'
)

# Parametro - Lenguaje de entrada
parser.add_argument(
    '-lengI',
    '--lenguage_input',
    help='Lenguage import input'
)

# Parametro - Lenguaje de salida
parser.add_argument(
    '-lengO',
    '--lenguage_output',
    help='Lenguage export output'
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
    if pathlib(args.input_text).exists():
        return args.input_text
    else:
        print('ERROR - This is not a file')

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
    
# Evento - Parametro lenguage input
def lenguage_input():
    try:
        return args.lenguage_input
    except:
        print('ERROR - Select a input lenguage')

# Evento - Parametro lenguage output
def lenguage_output():
    try:
        return(args.lenguage_output)
    except:
        print('ERROR - Select a output lenguage')


# Texto a traducir
def Translate_and_save():
    if input_text() == None:
        # Si el archivo a traducir no existe
        pass
    else:
        # Si existe el archivo
        try:
            text_file = Text_Read(
                file_and_path=input_text(),
                opc='ModeText'
            )
        except:
            print('ERROR - This is not a text file')
            pass

        # Objeto - Traductor
        if (
            lenguage_input() == None or
            lenguage_output() == None
        ):
            # Si no existe los lenguages de input o output
            print('ERROR - Lenguege input or output, not goods')
        else:
            translator = GoogleTranslator(
                source=lenguage_input(),
                target=lenguage_output()
            )

            # Traduccion de texto a traducir
            text_translate = translator.translate(text_file)

            # Mostrar texto original
            # Mostrar texto traducido
            print(
                Title(lenguage_input(), see=False) +
                text_file + '\n\n' +

                Title(lenguage_output(), see=False) +
                text_translate + '\n\n'+
                
                Separator(see=False)
            )

            try:
                with open(args.output_text, 'w') as text_output:
                    text_output.write(text_translate)
            except:
                print('WARNING - Output not good')
                
            print("Translated - That's good")


# Ejecutar programa y salir
try:
    Translate_and_save()
except:
    print('ERROR - Parameters, not goods')