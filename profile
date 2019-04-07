# Misc env variables
export QT_QPA_PLATFORMTHEME="qt5ct"
export EDITOR=/usr/bin/vim
export VISUAL=$EDITOR
export GTK2_RC_FILES="$HOME/.gtkrc-2.0"
export BROWSER=/usr/bin/firefox
export DOTFILES=$HOME/.dotfiles
export SCRIPTS=$DOTFILES/scripts
export CONFIG=$HOME/.config

# PATH stuff
export PATH=$SCRIPTS:$PATH
## Ruby
export PATH="$PATH:$(ruby -e 'puts Gem.user_dir')/bin"

# Misc customization options
## Used for my pywal script to set the alpha value for URXVT
export TERM_ALPHA=90
## Allows to close Steam to tray
export STEAM_FRAME_FORCE_CLOSE=1
## Sets the lastpass session to not timeout
export LPASS_AGENT_TIMEOUT=0


systemctl --user import-environment PATH

# Source .bashrc explicitly if connected through SSH
[[ -n "$SSH_CLIENT" ]] && source $HOME/.bashrc

# Sets wallpaper on startup if the script exists. This step is ignored if connected through SSH
[[ -f $SCRIPTS/set_wallpaper && ! -n "$SSH_CLIENT" ]] && set_wallpaper
