#!/bin/bash

echo "# acca-video-series" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/pj0620/acca-video-series.git
git push -u origin master
