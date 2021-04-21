rahr
====

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
Pick: 
1
magnet:?xt=urn:btih:1234567890&dn=Big.Buck.Bunny.720p&tr=http%3A%2F%2Ftracker.trackerfix.com%3A80%2Fannounce
$ rahr --help
usage: rahr [-h] [--choice CHOICE] [--peerflix] [--jackett-host JACKETT_HOST] [--jackett-api-key JACKETT_API_KEY]
            [--jackett-indexer JACKETT_INDEXER]
            search [search ...]

positional arguments:
  search

optional arguments:
  -h, --help            show this help message and exit
  --choice CHOICE
  --peerflix            If present, calls peerflix with the selected link. If env variable PEERFLIX_PLAYER is set, launches
                        given player, otherwise video streams on <local ip>:8888
  --jackett-host JACKETT_HOST
                        Specify jackett host in form host:port. Defaults to localhost:9117. can also be provided with
                        JACKETT_HOST
  --jackett-api-key JACKETT_API_KEY
                        Specify jackett API key. can also be provided with JACKETT_API_KEY
  --jackett-indexer JACKETT_INDEXER
                        Specify jackett indexer. Defaults to 'all'
```
