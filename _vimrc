source $VIMRUNTIME/delmenu.vim
set langmenu=none
source $VIMRUNTIME/menu.vim

" Отключение режима совместимости со старыми версиями
set nocompatible

"My key mappings
source $HOME/mappings.vim
source $HOME/functions.vim
set viewdir=$HOME/view

if version >= 700
    set history=64
    set undolevels=128
    set undodir=$HOME/.vim/undodir/
    set undofile
    set undolevels=1000
    set undoreload=10000
endif

" Без резервных копий
set nobackup

" Без временного файла
set noswapfile

" Размер истории командной строки
set history=50

" Линейка
set ruler

" Отображать команду в статусной строке
set showcmd

" Перенос длинных строк
set wrap

" Перенос целых слов
set linebreak

" Номера строк
set number

" Поддерка мыши
set mouse=a

" Подсветка синтаксиса
syntax on

abbreviate li «
abbreviate ri »

" При скорочтении полезно выделять союзы
match Comment /\<[Ее]сли\>\|\<[Дд]а\>\|\<не только\>\|\<[Ии]\>\|\<либо\>\|\<то\>\|\<не то\>\|\<потому что\>\|\<оттого\>\|\<оттого\>\|\<[Чч]тобы\>\|\<[Пп]оэтому\>\|\<[Нн]о\>\|\<[Кк]ак\>\|\<[Бб]удто\>\|\<[Тт]ак\>\|\<[Кк]огда\>\|\<[Ее]два\>\|\<[Тт]аким образом\>\|\<[Ии]ли\>\|\<[Дд]ля того\>\|\<[Чч]то\>\|\<[Тт]акже\>\|\<[Тт]оже\>\|\<[Зз]ато\>\|\<[Оо]днако\>/

2match ErrorMsg /\s\+$/

" ==================================
" Поиск
" ==================================

" Подцветка соответствий шаблону поиска
set hlsearch

" При поиске перескакивать на найденный текст в процессе набора строки
set incsearch

" Игнорировать регистр символов
set ignorecase

" для некоторых типов файлов настройки отступов были перенесены из plugin в
" indent. Поэтому не забывайте делать :filetype plugin indent on в вашем
" .vimrc.
" Синтаксис на основе расширения файла
filetype plugin indent on

" Автоотступ
set autoindent

" Шрифт
set guioptions=remgLt
"set guifont=Lucida_Console:h14:cRUSSIAN
"set guifont=Consolas:h14:cRUSSIAN
"set guifont=Lucida_Console:h18:cRUSSIAN
"set guifont=Consolas:h14:cRUSSIAN
set guifont=DejaVu_Sans_Mono:h12:cRUSSIAN

"set guifont=Consolas:h18:cRUSSIAN
"set guifont=Consolas:h20:cRUSSIAN
set printfont=Lucida_Console:h11:cRUSSIAN
"set guifont=Courier_New:h12:cRUSSIAN

" Цветовая схема
"colorscheme darkblue
"colorscheme gmt2
"colorscheme ron
colorscheme st
"colorscheme default

"colorscheme ron

" Корректное распознавание русских букв
set iskeyword=@,a-z,A-Z,48-57,_,168,184,128-175,192-255

" Установка символов, которыми будет осуществляться подсветка
set nolist
"set list
"set listchars=eol:$,tab:»\ ,space:·
"set lcs=eol:$,tab:»\ ,trail:·

set laststatus=0
set statusline=%F%m%r%h%w\ [FORMAT=%{&ff}]\ [TYPE=%Y]\ [ASCII=\%03.3b]\ [HEX=\%02.2B]\ [POS=%04l,%04v][%p%%]\ [LEN=%L]

" Добавление клавиш Windows
source $VIMRUNTIME/mswin.vim

" Не ругаться на несохраненный буфер,
" при переключении буферов
set hidden

set tw=70

"More visual cursor
set nocursorline

set foldmethod=marker
set foldcolumn=0

set formatprg=par\ -w70rjq

let g:html_use_css=0
let g:html_no_foldcolumn = 1
let g:html_number_lines = 0


" Disable blinking cursor
set guicursor=a:blinkon0

"call pathogen#infect()

"set background=dark
"colorscheme solarized
"
set tabstop=4

function! Serg()
    silent! normal V
endfunction

command! FreemindText call Serg()

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


nnoremap <Space> i<Space><Esc>

"set ic!
"set gfn=Calibri:h14:cDEFAULT
"set fenc=utf-8
"set encoding=utf-8
"set wrap!
"
nnoremap <F6> "=strftime("%H:%M")<CR>P
inoremap <F6> <C-R>=strftime("%H:%M")<CR>

" key map problems in russian (vimLatex)
imap <C-b> <Plug>Tex_MathBF
imap <C-c> <Plug>Tex_MathCal
imap <C-l> <Plug>Tex_LeftRight
imap <C-i> <Plug>Tex_InsertItemOnThisLine

"set encoding=utf8
"set fileencodings=utf8,cp1251
