# How to working with my rep

##1 Create a new remote branch

git clone git@github.com:Stivi/MyDocs.git

cd MyDocs

git checkout -b [name-of-branch]

git add flac_ape_m4a_wv_to-ogg.bat

git commit -m 'all to ogg'

git push --set-upstream origin [name-of-branch]

git remote show origin

##2 Copy remote branch

git clone git@github.com:Stivi/MyDocs.git

cd MyDocs

git remote show origin

git checkout --track origin/multim[TAB]

##3 Resetting the repository (no repeat)

git init

git add .

git commit -m 'Initial commit'

git remote add origin git@github.com:Stivi/MyDocs.git

git push --force
