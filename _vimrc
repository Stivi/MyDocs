" Меню на английском
source $VIMRUNTIME/delmenu.vim
set langmenu=none
source $VIMRUNTIME/menu.vim

" Отключение режима совместимости со старыми версиями
set nocompatible

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

" Размер истории командной строки
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
match Comment /\<[Ее]сли\>\|\<[Дд]а\>\|\<не только\>\|\<[Ии]\>\|\<либо\>\|\<то\>\|\<не то\>\|\<потому что\>\|\<оттого\>\|\<оттого\>\|\<[Чч]тобы\>\|\<[Пп]оэтому\>\|\<[Нн]о\>\|\<[Кк]ак\>\|\<[Бб]удто\>\|\<[Тт]ак\>\|\<[Кк]огда\>\|\<[Ее]два\>\|\<[Тт]аким образом\>\|\<[Ии]ли\>\|\<[Дд]ля того\>\|\<[Чч]то\>\|\<[Тт]акже\>\|\<[Тт]оже\>\|\<[Зз]ато\>\|\<[Оо]днако\>/

2match ErrorMsg /\s\+$/

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
set guioptions=regLt
set guifont=DejaVu_Sans_Mono:h12:cRUSSIAN
set printfont=Lucida_Console:h11:cRUSSIAN

" Цветовая схема
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
