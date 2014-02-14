@ECHO OFF

set flac="c:\Program Files (x86)\Exact Audio Copy\Flac\flac.exe"
set oggenc="c:\Users\Sergey\Documents\Programs\oggenc2.87-1.3.3-x64\oggenc2.exe"
set mac="c:\Program Files\Monkey's Audio\MAC.exe"
set mplayer="c:\Program Files\mplayer\mplayer.exe"

CLS
IF EXIST *.pk DEL *.pk

echo Начало: > log
echo %DATE% >> log
echo %TIME% >> log

FOR %%I IN (*.flac) DO (%flac% -d -F "%%I" && DEL "%%I")

FOR %%I IN (*.ape) DO (%mac% "%%I" "%%I.wav" -d && DEL "%%I")

FOR %%I IN (*.m4a,*.wv) DO (%mplayer% -vc null -vo null -ao pcm:waveheader:file="%%I".wav "%%I" && DEL "%%I")

FOR %%I IN (*.wav) DO (%oggenc% --quality 5 "%%I" && DEL "%%I")

echo Конец: >> log
echo %DATE% >> log
echo %TIME% >> log
