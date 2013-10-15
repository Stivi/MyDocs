
" Прямая речь для латекса
function! MySpeachFormat()
    silent! %s+^-+"--*+g
    silent! %s+ - + --- +g
    silent! %s+ -$+ ---+g
endfunction

command! MySpeach call MySpeachFormat()

" Восстановление позиции окна
au BufWinLeave *.* mkview
au BufWinEnter *.* silent loadview

" Восстановление позиции курсора
autocmd BufReadPost *
        \ if line("'\"") > 0 && line("'\"") <= line("$") |
        \      exe "normal g`\"" |
        \ endif
