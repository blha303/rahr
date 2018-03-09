rahr
====

A simple Python 3 program to reduce the number of keystrokes needed to get a torrent.

Installation
------------

```bash
$ pip3 install rahr
or
$ pip3 install git+https://github.com/blha303/rahr
```


Usage
-----

```
$ rahr big buck bunny
0: Big.Buck.Bunny.1080p (Movies/Legal)
1: Big.Buck.Bunny.720p (Movies/Legal)
Pick: (type 1)
magnet:?xt=urn:btih:1234567890&dn=Big.Buck.Bunny.720p&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce
$ rahr --help
usage: rahr [-h] [--choice CHOICE] [--peerflix] search [search ...]

positional arguments:
  search

optional arguments:
  -h, --help       show this help message and exit
  --choice CHOICE
  --peerflix       If present, calls peerflix with the selected magnet link.
                   If env variable PEERFLIX_PLAYER is set, launches given
                   player, otherwise video streams on <local ip>:8888
```

I'm not responsible for how you decide to use this program. I made it as an exercise only.
