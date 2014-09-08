set root="%HOMEDRIVE%%HOMEPATH%"
CD /D %root%
call git commit -a -m "%DATE% %TIME%"
call git push
