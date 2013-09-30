
" Разделяет абзацы"{{{
function! MyFormatTextFunction()
    silent! set tw=78
    silent! %s/$/\r/g
    silent! %s/^\n\+/\r/g
    silent! normal gggwG
    silent! %left 0
endfunction

command! MyFormatText call MyFormatTextFunction()
"}}}

" Прямая речь для латекса
function! MySpeachFormat()
    silent! %s/^-/"--*/g
    silent! %s/ - / --- /g
    silent! %s/ -$/ ---/g
endfunction

command! MySpeach call MySpeachFormat()

" Восстановление позиции окна
au BufWinLeave *.* mkview
au BufWinEnter *.* silent loadview
"au BufWinEnter *.txt colorscheme st
"au BufReadPost *.txt call MyTxtSettings()

" Восстановление позиции курсора
autocmd BufReadPost *
        \ if line("'\"") > 0 && line("'\"") <= line("$") |
        \      exe "normal g`\"" |
        \ endif

" fun MyCSSSettings()
"       set guifont=Lucida_Console:h12:cRUSSIAN
"       colorscheme gmt2
" endfun

"au BufReadPost *.css call MyCSSSettings()
"au BufReadPost *.html call MyCSSSettings()

" Go to last file(s) if invoked without arguments.

" autocmd VimLeave * nested if (!isdirectory($HOME . "/.vim")) |
"     \ call mkdir($HOME . "/.vim") |
"     \ endif |
"     \ execute "mksession! " . $HOME . "/.vim/Session.vim"
"
" autocmd VimEnter * nested if argc() == 0 && filereadable($HOME . "/.vim/Session.vim") |
"     \ execute "source " . $HOME . "/.vim/Session.vim"
