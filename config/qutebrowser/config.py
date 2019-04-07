# vim: ft=python fileencoding=utf-8 sts=4 sw=4 et:

# Copyright 2014-2018 Florian Bruhin (The Compiler) <mail@qutebrowser.org>
#
# This file is part of qutebrowser.
#
# qutebrowser is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# qutebrowser is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with qutebrowser.  If not, see <http://www.gnu.org/licenses/>.

# Imports and shit
import yaml
from socket import gethostname as hostname

# Importing pywal color settings

with (config.configdir / 'colors.yml').open() as f:
    yaml_data = yaml.load(f)

def dict_attrs(obj, path=''):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from dict_attrs(v, '{}.{}'.format(path, k) if path else k)
    else:
        yield path, obj

for k, v in dict_attrs(yaml_data):
    config.set(k, v)


## This is here so configs done via the GUI are still loaded.
## Remove it to not load settings done via the GUI.
config.load_autoconfig()


## The backend to use to display websites. qutebrowser supports two
## different web rendering engines / backends, QtWebKit and QtWebEngine.
## QtWebKit was discontinued by the Qt project with Qt 5.6, but picked up
## as a well maintained fork: https://github.com/annulen/webkit/wiki -
## qutebrowser only supports the fork. QtWebEngine is Qt's official
## successor to QtWebKit. It's slightly more resource hungry that
## QtWebKit and has a couple of missing features in qutebrowser, but is
## generally the preferred choice. This setting requires a restart.
## Type: String
## Valid values:
##   - webengine: Use QtWebEngine (based on Chromium)
##   - webkit: Use QtWebKit (based on WebKit, similar to Safari)
c.backend = 'webengine'


## Aliases for commands. The keys of the given dictionary are the
## aliases, while the values are the commands they map to.
## Type: Dict
c.aliases = {'w': 'session-save', 'q': 'quit', 'wq': 'quit --save'}


## Session autosave settings
c.auto_save.interval = 15000
c.auto_save.session = True    


## Color gradient interpolation system for download backgrounds.
## Type: ColorSystem
## Valid values:
##   - rgb: Interpolate in the RGB color system.
##   - hsv: Interpolate in the HSV color system.
##   - hsl: Interpolate in the HSL color system.
##   - none: Don't show a gradient.
c.colors.downloads.system.bg = 'rgb'
## Color gradient interpolation system for download text.
c.colors.downloads.system.fg = 'rgb'
## Color gradient interpolation system for the tab indicator.
c.colors.tabs.indicator.system = 'rgb'


## Autocompletion and history
## How many commands to save in the command history. 0: no history / -1:
## unlimited
## Type: Int
c.completion.cmd_history_max_items = 100
## The height of the completion, in px or as percentage of the window.
## Type: PercOrInt
c.completion.height = '50%'
## Move on to the next part when there's only one possible completion
## left.
## Type: Bool
c.completion.quick = True
## Padding of scrollbar handle in the completion window (in px).
## Type: Int
c.completion.scrollbar.padding = 2
## Width of the scrollbar in the completion window (in px).
## Type: Int
c.completion.scrollbar.width = 12
## When to show the autocompletion window.
## Type: String
## Valid values:
##   - always: Whenever a completion is available.
##   - auto: Whenever a completion is requested.
##   - never: Never.
c.completion.show = 'always'
## Shrink the completion to be smaller than the configured size if there
## are no scrollbars.
## Type: Bool
c.completion.shrink = False
## How to format timestamps (e.g. for the history completion).
## Type: TimestampTemplate
c.completion.timestamp_format = '%Y-%m-%d'
## How many URLs to show in the web history. 0: no history / -1:
## unlimited
## Type: Int
c.completion.web_history.max_items = -1

## Cache and cookies
c.content.cache.size = None
## Control which cookies to accept.
## Type: String
## Valid values:
##   - all: Accept all cookies.
##   - no-3rdparty: Accept cookies from the same origin only.
##   - no-unknown-3rdparty: Accept cookies from the same origin only, unless a cookie is already set for the domain.
##   - never: Don't accept cookies at all.
c.content.cookies.accept = 'no-3rdparty'
c.content.cookies.store = True


## Content blocking
c.content.host_blocking.enabled = True
## List of URLs of lists which contain hosts to block.  The file can be
## in one of the following formats:  - An `/etc/hosts`-like file - One
## host per line - A zip-file of any of the above, with either only one
## file, or a file named   `hosts` (with any extension).
## Type: List of Url
c.content.host_blocking.lists = ['https://www.malwaredomainlist.com/hostslist/hosts.txt', 'http://someonewhocares.org/hosts/hosts', 'http://winhelp2002.mvps.org/hosts.zip', 'http://malwaredomains.lehigh.edu/files/justdomains.zip', 'https://pgl.yoyo.org/adservers/serverlist.php?hostformat=hosts&mimetype=plaintext']
## List of domains that should always be loaded, despite being ad-
## blocked. Domains may contain * and ? wildcards and are otherwise
## required to exactly match the requested domain. Local domains are
## always exempt from hostblocking.
## Type: List of String
c.content.host_blocking.whitelist = ['piwik.org']


## Headers
c.content.headers.accept_language = 'en-US,en'
c.content.headers.custom = {}
c.content.headers.do_not_track = True
## Send the Referer header. The Referer header tells websites from which
## website you were coming from when visting them.
## Type: String
## Valid values:
##   - always: Always send the Referer.
##   - never: Never send the Referer. This is not recommended, as some sites may break.
##   - same-domain: Only send the Referer for the same domain. This will still protect your privacy, but shouldn't break any sites.
c.content.headers.referer = 'same-domain'
c.content.headers.user_agent = None


## Javascript
c.content.javascript.alert = True
c.content.javascript.can_access_clipboard = False
c.content.javascript.can_open_tabs_automatically = False
c.content.javascript.enabled = True
c.content.javascript.log = {'unknown': 'debug', 'info': 'debug', 'warning': 'debug', 'error': 'debug'}
c.content.javascript.modal_dialog = True
c.content.javascript.prompt = True


## Local content
c.content.local_content_can_access_file_urls = True
c.content.local_content_can_access_remote_urls = False
c.content.local_storage = True


## Proxy
## The proxy to use. In addition to the listed values, you can use a
## `socks://...` or `http://...` URL.
## Type: Proxy
## Valid values:
##   - system: Use the system wide proxy.
##   - none: Don't use any proxy
c.content.proxy = 'system'


## Download settings
## The directory to save downloads to. If unset, a sensible os-specific
## default is used.
## Type: Directory
c.downloads.location.directory = None
## Prompt the user for the download location. If set to false,
## `downloads.location.directory` will be used.
## Type: Bool
c.downloads.location.prompt = True
## Remember the last used download directory.
## Type: Bool
c.downloads.location.remember = True
## What to display in the download filename input.
## Type: String
## Valid values:
##   - path: Show only the download path.
##   - filename: Show only download filename.
##   - both: Show download path and filename.
c.downloads.location.suggestion = 'path'
## The default program used to open downloads. If null, the default
## internal handler is used. Any `{}` in the string will be expanded to
## the filename, else the filename will be appended.
## Type: String
c.downloads.open_dispatcher = None
## Where to show the downloaded files.
## Type: VerticalPosition
## Valid values:
##   - top
##   - bottom
c.downloads.position = 'top'
## Number of milliseconds to wait before removing finished downloads. If
## set to -1, downloads are never removed.
## Type: Int
c.downloads.remove_finished = 500


## Fonts
c.fonts.completion.category = 'bold 10pt monospace'
c.fonts.completion.entry = '10pt monospace'
c.fonts.debug_console = '10pt monospace'
c.fonts.downloads = '10pt monospace'
c.fonts.hints = 'bold 10pt monospace'
c.fonts.keyhint = '10pt monospace'
c.fonts.messages.error = '10pt monospace'
c.fonts.messages.info = '10pt monospace'
c.fonts.messages.warning = '10pt monospace'
c.fonts.monospace = '"xos4 Terminus", Terminus, Monospace, "DejaVu Sans Mono", Monaco, "Bitstream Vera Sans Mono", "Andale Mono", "Courier New", Courier, "Liberation Mono", monospace, Fixed, Consolas, Terminal'
c.fonts.prompts = '10pt sans-serif'
c.fonts.statusbar = '10pt monospace'
c.fonts.tabs = '10pt monospace'
c.fonts.web.family.cursive = ''
c.fonts.web.family.fantasy = ''
c.fonts.web.family.fixed = 'MesloLGL Nerd Font Mono'
c.fonts.web.family.sans_serif = 'SFNS Display'
c.fonts.web.family.serif = 'Linux Libertine'
c.fonts.web.family.standard = 'SFNS Display'
c.fonts.web.size.default_fixed = 13
c.fonts.web.size.minimum = 0
c.fonts.web.size.minimum_logical = 6

### device specific fonts config
if hostname() == "dauntless":
    c.fonts.web.size.default = 16
if hostname() == "vanguard":
    c.fonts.web.size.default = 18


## Hints
c.hints.auto_follow = 'always'
c.hints.auto_follow_timeout = 0
c.hints.chars = 'asdfghjkl'
c.hints.hide_unmatched_rapid_hints = True
c.hints.min_chars = 1
c.hints.mode = 'letter'
c.hints.next_regexes = ['\\bnext\\b', '\\bmore\\b', '\\bnewer\\b', '\\b[>→≫]\\b', '\\b(>>|»)\\b', '\\bcontinue\\b', '\\b[« Newer]\\b']
c.hints.prev_regexes = ['\\bprev(ious)?\\b', '\\bback\\b', '\\bolder\\b', '\\b[<←≪]\\b', '\\b(<<|«)\\b', '\\b[Older »]\\b']
c.hints.scatter = True
c.hints.uppercase = False

## Scrolling
c.scrolling.smooth = True


## Spell checking
## You can check for available languages and
## install dictionaries using scripts/install_dict.py. Run the script
## with -h/--help for instructions.
## Type: List of String
## Valid values:
##   - af-ZA: Afrikaans (South Africa)
##   - bg-BG: Bulgarian (Bulgaria)
##   - ca-ES: Catalan (Spain)
##   - cs-CZ: Czech (Czech Republic)
##   - da-DK: Danish (Denmark)
##   - de-DE: German (Germany)
##   - el-GR: Greek (Greece)
##   - en-CA: English (Canada)
##   - en-GB: English (United Kingdom)
##   - en-US: English (United States)
##   - es-ES: Spanish (Spain)
##   - et-EE: Estonian (Estonia)
##   - fa-IR: Farsi (Iran)
##   - fo-FO: Faroese (Faroe Islands)
##   - fr-FR: French (France)
##   - he-IL: Hebrew (Israel)
##   - hi-IN: Hindi (India)
##   - hr-HR: Croatian (Croatia)
##   - hu-HU: Hungarian (Hungary)
##   - id-ID: Indonesian (Indonesia)
##   - it-IT: Italian (Italy)
##   - ko: Korean
##   - lt-LT: Lithuanian (Lithuania)
##   - lv-LV: Latvian (Latvia)
##   - nb-NO: Norwegian (Norway)
##   - nl-NL: Dutch (Netherlands)
##   - pl-PL: Polish (Poland)
##   - pt-BR: Portuguese (Brazil)
##   - pt-PT: Portuguese (Portugal)
##   - ro-RO: Romanian (Romania)
##   - ru-RU: Russian (Russia)
##   - sh: Serbo-Croatian
##   - sk-SK: Slovak (Slovakia)
##   - sl-SI: Slovenian (Slovenia)
##   - sq: Albanian
##   - sr: Serbian
##   - sv-SE: Swedish (Sweden)
##   - ta-IN: Tamil (India)
##   - tg-TG: Tajik (Tajikistan)
##   - tr-TR: Turkish (Turkey)
##   - uk-UA: Ukrainian (Ukraine)
##   - vi-VN: Vietnamese (Viet Nam)
c.spellcheck.languages = ['en-US']


## Tabs
c.tabs.background = True
c.tabs.close_mouse_button = 'middle'
c.tabs.favicons.scale = 1.0
c.tabs.indicator.padding = {'top': 2, 'bottom': 2, 'left': 0, 'right': 4}
c.tabs.padding = {'top': 0, 'bottom': 0, 'left': 5, 'right': 5}
c.tabs.last_close = 'close'
c.tabs.mousewheel_switching = True
c.tabs.new_position.related = 'next'
c.tabs.new_position.unrelated = 'last'
c.tabs.position = 'top'
c.tabs.select_on_remove = 'next'
c.tabs.show = 'multiple'
c.tabs.show_switching_delay = 800
c.tabs.tabs_are_windows = False
c.tabs.title.alignment = 'left'
c.tabs.title.format = '{index}: {title}'
c.tabs.title.format_pinned = '{index}'
c.tabs.width = '20%'
c.tabs.indicator.width = 3
c.tabs.wrap = True


## Search
config.source('searchengines.py')

## Zoom
c.zoom.default = '100%'
c.zoom.levels = ['25%', '33%', '50%', '67%', '75%', '90%', '100%', '110%', '125%', '150%', '175%', '200%', '250%', '300%', '400%', '500%']
c.zoom.mouse_divider = 512


## Content
c.confirm_quit = ['never']
c.content.default_encoding = 'iso-8859-1'
c.content.geolocation = 'ask'
c.content.hyperlink_auditing = False
c.content.images = True
c.content.media_capture = 'ask'
c.content.netrc_file = None
c.content.private_browsing = False
c.content.ssl_strict = 'ask'


## URL
c.url.auto_search = 'naive'
c.url.default_page = '~/.config/startpage/startpage.html'
c.url.start_pages = ['~/.config/startpage/startpage.html']
c.url.incdec_segments = ['path', 'query']
c.url.yank_ignored_parameters = ['ref', 'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content']


## Misc settings
c.window.title_format = '{perc}{title}{title_sep}qutebrowser'
c.search.ignore_case = 'smart'
c.editor.command = ['vim', '-f', '{}']

## New Instance
c.new_instance_open_target = 'tab'
c.new_instance_open_target_window = 'last-focused'

## Key bindings
config.source('bindings.py')
config.source('personal_bindings.py')
config.source('shortcuts.py')
