set encoding=utf-8
language messages en

" Меню на английском
source $VIMRUNTIME/delmenu.vim
set langmenu=none
source $VIMRUNTIME/menu.vim

" Включение поддержки русского языка
set keymap=russian-jcukenwin
set iminsert=0
set imsearch=0
highlight lCursor guifg=NONE guibg=Cyan

set viewdir=$HOME/view

"My key mappings
source $HOME/mappings.vim
source $HOME/functions.vim

if version >= 700
    set history=64
    set undolevels=128
    set undodir=$HOME/.vim/undodir/
    set undofile
    set undolevels=1000
    set undoreload=10000
endif

set nobackup
set noswapfile

set history=50

" Show the line and column number of the cursor position
set ruler

" Отображать команду в статусной строке
set showcmd

set wrap
set linebreak
set textwidth=70

" Номера строк
set number

" Поддерка мыши
set mouse=a

" Подсветка синтаксиса
syntax on

abbreviate li «
abbreviate ri »

" При скорочтении полезно выделять союзы
match Comment
         \ /\<[Аа]\>
         \ \|\<[Бб]удто\>
         \ \|\<[Дд]а\>
         \ \|\<[Дд]ля того\>
         \ \|\<[Ее]два\>
         \ \|\<[Ее]сли\>
         \ \|\<[Зз]ато\>
         \ \|\<[Ии]\>
         \ \|\<[Ии]ли\>
         \ \|\<[Кк]ак\>
         \ \|\<[Кк]огда\>
         \ \|\<[Лл]ибо\>
         \ \|\<[Нн]е то\>
         \ \|\<[Нн]е только\>
         \ \|\<[Нн]и\>
         \ \|\<[Нн]о\>
         \ \|\<[Оо]днако\>
         \ \|\<[Оо]ттого\>
         \ \|\<[Пп]отому что\>
         \ \|\<[Пп]оэтому\>
         \ \|\<[Сс]ловно\>
         \ \|\<[Тт]ак\>
         \ \|\<[Тт]акже\>
         \ \|\<[Тт]аким образом\>
         \ \|\<[Тт]о\>
         \ \|\<[Тт]оже\>
         \ \|\<[Чч]то\>
         \ \|\<[Чч]тобы\>/

2match ErrorMsg /\s\+$/

" Подсветка соответствий шаблону поиска
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

set guioptions=regLt
set guifont=DejaVu_Sans_Mono:h12:cRUSSIAN
set printfont=Lucida_Console:h11:cRUSSIAN

colorscheme st

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

set hidden

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

set tabstop=4
