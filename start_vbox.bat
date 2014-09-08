@ECHO OFF

CLS

SET PUTTY="c:\Users\Sergey\Documents\Programs\Putty\PUTTY.EXE"
SET VBoxManage="c:\Program Files\Oracle\VirtualBox\VBoxManage.exe"


%VBoxManage% startvm sid
%PUTTY% -load "Debian" -l user -pw 99
%VBoxManage% controlvm sid savestate


COPY /Y d:\Stev\share\ideas\triz\genius\genius.pdf d:\Shared_books\Dropbox\genius.pdf
