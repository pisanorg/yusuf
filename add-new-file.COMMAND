#!/bin/bash

cd /Users/pisan/bitbucket/www
git pull
date > all-files.txt
ls -lR >> all-files.txt
git add all-files.txt files/*
git commit -m "new files"; git push

echo "https://pisanorg.github.io/yusuf/all-files.txt"
