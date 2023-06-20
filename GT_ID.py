import argparse
from pathlib import Path as pathlib
from Modulos.Modulo_GT import Translate


# Objeto para los parametros
parser = argparse.ArgumentParser()

# Parametro - File
parser.add_argument(
    '-i',
    '--input_text',
    help='Text input'
)

# Parametro - ID
parser.add_argument(
    '-id',
    '--id_number',
    help='Text ID'
)

# Parametro - Text Only
parser.add_argument(
    '-t',
    '--text_only',
    help='Text type String'
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

# Parametro - File output
parser.add_argument(
    '-o',
    '--output_text',
    help='Text Output'
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


# Evento - Parametro id
def id_number():
    try:
        # Verificar que sea un numero
        if float(args.id_number):
            pass

        # Alistar id_li.txt
        return args.id_number

    except:
        pass
        #print('ERROR - This is not a number')

def id_input():
    if type( id_number() ) is str:
        return f'{id_number()}_{language_input()}.txt'
    else:
        pass

def id_output():
    if type( id_number() ) is str:
        return f'{id_number()}_{language_output()}.txt'
    else:
        pass


# Evento - Parametro texto only
def text_only():
    return args.text_only

    
# Evento - Parametro language input
def language_input():
    return args.language_input


# Evento - Parametro language output
def language_output():
    return(args.language_output)


# Texto a traducir
def output_text():
    return args.output_text


if (
    type (args.input_text) is str or
    type (args.id_number) is str or
    type (args.text_only) is str or
    type (args.language_input) is str or
    type (args.language_output) is str or
    type (args.output_text) is str
):
    Translate(
        input_text=input_text(),

        id_input=id_input(),
        id_output=id_output(),

        text_only=text_only(),

        language_input=language_input(),
        language_output=language_output(),

        output_text=output_text(),

        print_mode=True
    )
else:
    print('-h  or --help, to help')