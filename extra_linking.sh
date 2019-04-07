#!/bin/bash

DOTFILES=$HOME/.dotfiles
SYNC=$DOTFILES/private_sync
CONFIG=$HOME/.config

## Performs some extra symlinks that can't easily be handler by dotbot (or that I haven't figured out how to do)

# qutebrowser custom theme with pywal colors
if [[ ! -f $HOME/.config/qutebrowser/colors.yml && -f $HOME/.cache/wal/qutebrowser.yml ]]
then
	ln -s $HOME/.cache/wal/qutebrowser.yml $HOME/.config/qutebrowser/colors.yml
fi


# Taskbook files
[[ ! -f $HOME/.taskbook.json ]] && ln -s $SYNC/taskbook.json $HOME/.taskbook.json
[[ ! -f $HOME/.taskbook ]] && ln -s $SYNC/taskbook $HOME/.taskbook


# Rclone private settings
[[ ! -f $CONFIG/rclone ]] && ln -s $SYNC/rclone $CONFIG/rclone

# Symlinking gpg keyring
[[ ! -f $HOME/.gnupg ]] && ln -s $SYNC/gnupg $HOME/.gnupg
