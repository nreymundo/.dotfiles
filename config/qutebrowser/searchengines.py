## Search
## Definitions of search engines which can be used via the address bar.
## Maps a searchengine name (such as `DEFAULT`, or `ddg`) to a URL with a
## `{}` placeholder. The placeholder will be replaced by the search term,
## use `{{` and `}}` for literal `{`/`}` signs. The searchengine named
## `DEFAULT` is used when `url.auto_search` is turned on and something
## else than a URL was entered to be opened. Other search engines can be
## used by prepending the search engine name to the search term, e.g.
## `:open google qutebrowser`.
## Type: Dict
c.url.searchengines = {
        'DEFAULT': 'https://www.google.com/search?&q={}',
        'ddg': 'https://duckduckgo.com/?q={}',
        'i': 'https://duckduckgo.com/?q={}&iar=images&iax=images&ia=images',
        'red': 'https://reddit.com/r/{}',
        'tw': 'https://twitter.com/{}',
        '8': 'https://8ch.net/{}',
        'aw': 'https://wiki.archlinux.org/index.php?title=Special%3ASearch&search={}',
        '4cat': 'https://boards.4chan.org/{}/catalog',
        'w': 'https://www.wikipedia.org/search-redirect.php?family=wikipedia&language=en&search={}&language=en&go=Go',
        '4': 'https://boards.4chan.org/{}',
        'vw': 'http://vim.wikia.com/wiki/Special:Search?fulltext=Search&query={}',
        'ht': 'https://hooktube.com/results?search_query={}',
        'yt': 'https://youtube.com/search?q={}',
        }

