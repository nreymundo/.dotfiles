# Sourcing .zprofile on each startup so everything behaves as a login shell because reasons
if [ -f ~/.zprofile ]; then
	source ~/.zprofile
fi

# Sourcing personal aliases
source $CONFIG/shell_aliases

# Antigen main file
source $DOTFILES/antigen.zsh

# Load the oh-my-zsh's library.
antigen use oh-my-zsh

# Bundles from the default repo (robbyrussell's oh-my-zsh).
antigen bundle git
antigen bundle heroku
antigen bundle pip
antigen bundle lein
antigen bundle command-not-found

# Syntax highlighting bundle.
#antigen bundle zsh-users/zsh-syntax-highlighting
#antigen bundle zsh-users/zsh-autosuggestions

# Load the theme.
#antigen theme robbyrussell
antigen theme denysdovhan/spaceship-prompt
#antigen theme agnoster

# Tell Antigen that you're done.
antigen apply

# Pywal stuff
(cat $HOME/.cache/wal/sequences &)
source $HOME/.cache/wal/colors-tty.sh
source $HOME/.cache/wal/colors.sh

# System info with neofetch
neofetch
