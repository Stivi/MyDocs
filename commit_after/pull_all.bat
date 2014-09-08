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
echo pull_start:>> c:\log
echo %DATE%>> c:\log
echo %TIME%>> c:\log

CD /D %git_vim%
call git pull

CD /D %git_books%
call git pull

CD /D %git_multimedia%
call git pull

CD /D %git_python%
call git pull

CD /D %git_scripts%
call git pull

CD /D %bucket_books%
call git pull

CD /D %bucket_ledger%
call git pull

echo ---------->> c:\log
echo pull_end:>> c:\log
echo %DATE%>> c:\log
echo %TIME%>> c:\log
