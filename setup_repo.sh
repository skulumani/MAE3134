#!/bin/bash

# add the correct remote repositories
git_repo="git@github.com:skulumani/MAE3134_Spring2017_syllabus.git"
bb_repo="git@bitbucket.org:shankarkulumani/MAE3134_Spring2017_syllabus.git"
fdcl_repo="git@github.com:fdcl-gwu/MAE3134_Spring2017_syllabus.git"

printf "Setting the origin remote to point to Github and Bitbucket:\n\n"
printf "Github: $git_repo\n"
printf "Bitbucket: $bb_repo\n"
printf "FDCL: $fdcl_repo\n\n"

git remote set-url origin --push --add $bb_repo
git remote set-url origin --push --add $fdcl_repo
git remote set-url origin --push --add $git_repo

printf "Finished! The new remotes are listed.\n"
printf "\n"

git remote -v