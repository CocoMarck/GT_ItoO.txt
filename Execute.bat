cls


echo .\GT_ID.exe -h

.\GT_ID.exe -h
pause


cls
echo .\GT_ID.exe -i .\Archivos_base\ -id 10.1 -li es -lo en -o .\Archivos_traducidos\

.\GT_ID.exe -i .\Archivos_base\ -id 10.1 -li es -lo en -o .\Archivos_traducidos\
pause


cls
echo .\GT_ID.exe -id 10 -li es -lo en

.\GT_ID.exe -id 10 -li es -lo en
pause


cls
echo .\GT_ID.exe -t "Texto necesario" -li es -lo en

.\GT_ID.exe -t "Texto necesario" -li es -lo en
pause


cls
echo .\GT_ID.exe -t "Texto necesario" -li es -lo en -o .\OnlyText_en.txt

.\GT_ID.exe -t "Texto necesario" -li es -lo en -o .\OnlyText_en.txt
pause


cls
echo .\GT_ID.exe -i .\Texto_es.txt -li es -lo en

.\GT_ID.exe -i .\Texto_es.txt -li es -lo en
pause


cls
echo .\GT_ID.exe -i .\Texto_es.txt -li es -lo en -o .\Text_en.txt

.\GT_ID.exe -i .\Texto_es.txt -li es -lo en -o .\Text_en.txt
pause