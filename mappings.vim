
" ==========================
" Привязки к клавишам
" ==========================

noremap <F2>            :update<CR>
vnoremap <F2>           <C-C>:update<CR>
inoremap <F2>           <C-O>:update<CR>

" Переключение буферов по
" Ctrl+PgUP,PageDown
nmap <C-PageUP> :bnext!<CR>
nmap <C-PageDown> :bprevious!<CR>

nmap <F4> o<Esc>
nmap <F5> gqap

map <MiddleMouse> z<CR>
imap <MiddleMouse> z<CR>

map <F12> z<CR>
imap <F12> z<CR>

map <F5> gqap
imap <F5> gqap

" Нажать Ctrl-N для выключения подцветки
nmap <silent> <C-N> :silent noh<CR>

" Удобное меню для переключения
" кодировки (F8)
set wildmenu
set wcm=<Tab>
menu Encoding.utf-8             :e ++enc=utf-8 <CR>
menu Encoding.windows-1251      :e ++enc=cp1251<CR>
menu Encoding.koi8-r            :e ++enc=koi8-r<CR>
menu Encoding.ibm-866           :e ++enc=ibm866<CR>
map <F8> :emenu Encoding.<TAB>


nnoremap <F6> "=strftime("%d %b %Y, %H:%M")<CR>Po
nnoremap <F7> "=strftime("%H:%M")<CR>Po

map <Up> gk
map <Down> gj

map <F3> :set fileencoding=cp1251<CR>{j :left 0<CR>gqip<Esc>:set fileencoding=utf-8<CR>
map <F10> ?
map <F11> :%s+++g<CR>
map <F9> vipgw

" по звездочке не прыгать на следующее найденное, а просто подсветить
nnoremap * *N

" выключить подсветку: повесить на горячую клавишу Ctrl-F8
nnoremap <C-F8> :nohlsearch<CR>

" в визуальном режиме по команде * подсвечивать выделение
vnoremap * y :execute ":let @/=@\""<CR> :execute "set hlsearch"<CR>

" Bubble single lines
nmap <C-Up> ddkP
nmap <C-Down> ddp
" Bubble multiple lines
vmap <C-Up> xkP`[V`]
vmap <C-Down> xp`[V`]

nnoremap <Space> i<Space><Esc>

" key map problems in russian (vimLatex)
imap <C-b> <Plug>Tex_MathBF
imap <C-c> <Plug>Tex_MathCal
imap <C-l> <Plug>Tex_LeftRight
imap <C-i> <Plug>Tex_InsertItemOnThisLine
