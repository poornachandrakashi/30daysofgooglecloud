#!/bin/bash
touch initial
git add initial
git commit -m "initial commit"
git push -u origin master
git add .
git commit -m "Updated Repository data"
git push origin master
