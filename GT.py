import argparse
from pathlib import Path as pathlib
from Modulo_GT import Translate


# Objeto para los parametros
parser = argparse.ArgumentParser()

# Parametro - File
parser.add_argument(
    '-i',
    '--input_text',
    help='Text input'
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
    type (args.text_only) is str or
    type (args.language_input) is str or
    type (args.language_output) is str or
    type (args.output_text) is str
):
    Translate(
        input_text=input_text(),

        text_only=text_only(),

        language_input=language_input(),
        language_output=language_output(),

        output_text=output_text(),

        print_mode=True
    )
else:
    print('-h  or --help, to help')