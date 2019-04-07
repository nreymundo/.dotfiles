#!/bin/bash

# Check if folder already exists and don't do anything if it does. 
[ -d $HOME/.vim/bundle/neobundle.vim ] && exit 0 

# Clones neobundle code
mkdir -p $HOME/.vim/bundle 
git clone https://github.com/Shougo/neobundle.vim $HOME/.vim/bundle/neobundle.vim
