clear


echo python3 GT_ID.py -h

python3 GT_ID.py -h
read -r -p 'Continuar'


clear
echo python3 GT_ID.py -i ./Archivos_base/ -id 10.1 -li es -lo en -o ./Archivos_traducidos/

python3 GT_ID.py -i ./Archivos_base/ -id 10.1 -li es -lo en -o ./Archivos_traducidos/
read -r -p 'Continuar'


clear
echo python3 GT_ID.py -id 10 -li es -lo en

python3 GT_ID.py -id 10 -li es -lo en
read -r -p 'Continuar'


clear
echo python3 GT_ID.py -t "Texto necesario" -li es -lo en

python3 GT_ID.py -t "Texto necesario" -li es -lo en
read -r -p 'Continuar'


clear
echo python3 GT_ID.py -t "Texto necesario" -li es -lo en -o ./OnlyText_en.txt

python3 GT_ID.py -t "Texto necesario" -li es -lo en -o ./OnlyText_en.txt
read -r -p 'Continuar'


clear
echo python3 GT_ID.py -i ./Texto_es.txt -li es -lo en

python3 GT_ID.py -i ./Texto_es.txt -li es -lo en
read -r -p 'Continuar'


clear
echo python3 GT_ID.py -i ./Texto_es.txt -li es -lo en -o ./Text_en.txt

python3 GT_ID.py -i ./Texto_es.txt -li es -lo en -o ./Text_en.txt
read -r -p 'Eso es todo...'