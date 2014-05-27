@ECHO OFF

SET FFMPEG="H:\d\Programs\last\ffmpeg-latest-win32-static\ffmpeg-20140104-git-adc09a3-win32-static\bin\ffmpeg.exe"
SET VCODECOPTIONS=-vcodec libx264 -profile baseline -level 13
SET SIZE=-r 24000/1001 -s 320x180
SET BITRATE=-bt 900k
SET AOPTIONS=-acodec libvo_aacenc -ab 48k

FOR %%I IN (*.mp4) DO (%FFMPEG% -i "%%I" %SIZE% %AOPTIONS% %VCODECOPTIONS% %BITRATE% -pass 1 outin.mp4)
