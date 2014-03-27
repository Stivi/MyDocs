
" Прямая речь для латекса
function! MySpeachFormat()
    silent! %s+^-+"--*+g
    silent! %s+ - + --- +g
    silent! %s+ -$+ ---+g
endfunction

command! MySpeach call MySpeachFormat()


" Delete all trailing whitespace (at the end of each line)
function! DelWhiteSpaces()
    silent! %s/\s\+$//
endfunction

command! DelWhiteSpace call DelWhiteSpaces()

" Восстановление позиции окна
autocmd BufWinLeave *.* mkview
autocmd BufWinEnter *.* silent loadview

" Восстановление позиции курсора
autocmd BufReadPost *
        \ if line("'\"") > 0 && line("'\"") <= line("$") |
        \      exe "normal g`\"" |
        \ endif

" Commiting after save
"BufWritePost * execute '! if [ -d .git ] || git rev-parse --git-dir > NUL 2>&1 ; then git add % ; git commit -m %; fi'
autocmd BufWritePost *
\   echo "the value of 'shell' is" &shell
"\   expand('<afile>:p:h').'/../'.expand('<afile>:t:r').'js'
