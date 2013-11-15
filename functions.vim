
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
au BufWinLeave *.* mkview
au BufWinEnter *.* silent loadview

" Восстановление позиции курсора
autocmd BufReadPost *
        \ if line("'\"") > 0 && line("'\"") <= line("$") |
        \      exe "normal g`\"" |
        \ endif
