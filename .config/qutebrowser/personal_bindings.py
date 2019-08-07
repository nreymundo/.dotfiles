## Download locations
config.bind(";;d", "set downloads.location.directory ~/Documents ;; hint links download")
config.bind(";;D", "set downloads.location.directory ~/Downloads ;; hint links download")
config.bind(";;m", "set downloads.location.directory ~/Music ;; hint links download")
config.bind(";;ii", "set downloads.location.directory ~/Images ;; hint images download")
config.bind(";;vv", "set downloads.location.directory ~/Videos ;; hint links download")
config.bind(";;s", "set downloads.location.directory ~/.scripts ;; hint links download")
config.bind(";;cf", "set downloads.location.directory ~/.config ;; hint links download")
###Reset downloads location and settings
config.bind("||rds", "set downloads.location.directory ~/Downloads ;; set downloads.location.prompt false")

## LastPass 
config.bind(';;lp', 'spawn --userscript qute-lastpass')

## Navigation
config.bind(';P', 'hint links fill :open -p {hint-url}')

## Youtube stuff
config.bind(';;ytd', 'hint links spawn youtube-dl --config-location "~/.config/youtube-dl/config_downloads" {hint-url}')
config.bind(';;ytD', 'hint --rapid links spawn youtube-dl --config-location "~/.config/youtube-dl/config_downloads" {hint-url}')
config.bind('m', 'hint links spawn umpv {hint-url}')
config.bind(';;m', 'hint --rapid links spawn umpv {hint-url}')
