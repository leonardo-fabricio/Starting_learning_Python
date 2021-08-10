echo 'digite o nome do commit:'
read commit

git add *
git status
git commit -m "$commit"
git push origin main