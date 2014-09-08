@ECHO OFF

CLS

set git_vim="%HOMEDRIVE%%HOMEPATH%"
set git_books="%HOMEDRIVE%%HOMEPATH%\github\books"
set git_multimedia="%HOMEDRIVE%%HOMEPATH%\github\multimedia"
set git_python="%HOMEDRIVE%%HOMEPATH%\github\python"
set git_scripts="%HOMEDRIVE%%HOMEPATH%\github\scripts"
set bucket_books="%HOMEDRIVE%%HOMEPATH%\bucket\books"
set bucket_ledger="%HOMEDRIVE%%HOMEPATH%\bucket\ledger"

echo ---------->> c:\log
echo push_start:>> c:\log
echo %DATE%>> c:\log
echo %TIME%>> c:\log


CD /D %git_vim%
call git commit -a -m "%DATE% %TIME%"
call git push

CD /D %git_books%
call git commit -a -m "%DATE% %TIME%"
call git push

CD /D %git_multimedia%
call git commit -a -m "%DATE% %TIME%"
call git push

CD /D %git_python%
call git commit -a -m "%DATE% %TIME%"
call git push

CD /D %git_scripts%
call git commit -a -m "%DATE% %TIME%"
call git push

CD /D %bucket_books%
call git commit -a -m "%DATE% %TIME%"
call git push

CD /D %bucket_ledger%
call git commit -a -m "%DATE% %TIME%"
call git push

echo ---------->> c:\log
echo push_stop:>> c:\log
echo %DATE%>> c:\log
echo %TIME%>> c:\log
