#!/bin/sh

DOTFILES=$HOME/.dotfiles
SYNC=$DOTFILES/private_sync
CONFIG=$HOME/.config

## Performs some extra symlinks that can't easily be handled by dotbot (or that I haven't figured out how to do)
# qutebrowser custom theme with pywal colors
ln -sfn $HOME/.cache/wal/qutebrowser.yml $HOME/.config/qutebrowser/colors.yml
ln -sfn $SYNC/qutebrowser/bookmarks $HOME/.config/qutebrowser/bookmarks
# Taskbook files
ln -sfn $SYNC/taskbook.json $HOME/.taskbook.json
ln -sfn $SYNC/taskbook $HOME/.taskbook
# Rclone private settings
ln -sfn $SYNC/rclone $CONFIG/rclone
# Symlinking gpg keyring
ln -sfn $SYNC/gnupg $HOME/.gnupg
# Symlinking VPN config stuff
ln -sfn $SYNC/vpn/providers $CONFIG/vpn
