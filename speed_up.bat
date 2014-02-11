@ECHO OFF

set ffmpeg="C:\Users\ssv\Documents\Programs\ffmpeg-latest-win32-static\bin\ffmpeg.exe"

CLS

echo Начало: > log
echo %DATE% >> log
echo %TIME% >> log

%ffmpeg% -f concat -i mylist.txt -filter:v "setpts=0.001*PTS" output.mkv

echo Конец: >> log
echo %DATE% >> log
echo %TIME% >> log
