# Misc env variables
export MAKEFLAGS="-j$(nproc)"
export GPG_TTY=$(tty)
export QT_QPA_PLATFORMTHEME="qt5ct"
export TERM=xterm-color
export TERMINAL=/usr/local/bin/st
export EDITOR=/usr/bin/vim
export VISUAL=$EDITOR
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
export BROWSER=/usr/bin/firefox
export DOTFILES=$HOME/.dotfiles
export SCRIPTS=$DOTFILES/scripts
export I3_SCRIPTS=$SCRIPTS/i3blocks
export CONFIG=$HOME/.config
export DEFAULT_USER=`whoami`

# PATH stuff
export PATH=$SCRIPTS:$PATH
## Ruby
export PATH="$PATH:$(ruby -e 'puts Gem.user_dir')/bin"
## NVM
source /usr/share/nvm/init-nvm.sh
## Deduplicate PATH
export PATH="$(perl -e 'print join(":", grep { not $seen{$_}++ } split(/:/, $ENV{PATH}))')"

# Misc customization options
## Used for my pywal script to set the alpha value for URXVT
export TERM_ALPHA=90
## Allows to close Steam to tray
export STEAM_FRAME_FORCE_CLOSE=1
## Sets the lastpass session to not timeout
export LPASS_AGENT_TIMEOUT=0


systemctl --user import-environment PATH
