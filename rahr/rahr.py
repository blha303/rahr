#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser
import sys
from subprocess import Popen
from distutils.spawn import find_executable
from os import environ as env

token = get("https://torrentapi.org/pubapi_v2.php?get_token=get_token").json()["token"]

def main():
    parser = ArgumentParser()
    parser.add_argument("search", nargs="+")
    parser.add_argument("--choice", type=int)
    parser.add_argument("--peerflix", help="If present, calls peerflix with the selected magnet link. If env variable PEERFLIX_PLAYER is set, launches given player, otherwise video streams on <local ip>:8888", action="store_true")
    args = parser.parse_args()
    def q():
        return get("https://torrentapi.org/pubapi_v2.php", params={"mode": "search", "search_string": " ".join(args.search), "token": token, "format": "json"}).json()
    query = q()
    if not query.get("torrent_results"):
        query = q() # Sometimes the search fails
    results = query.get("torrent_results")
    if results:
        for n,r in enumerate(results):
            print("{}: {} ({})".format(n, r["filename"], r["category"]), file=sys.stderr)
        if len(results) > 1:
            try:
                if args.choice is not None:
                    choice = results[args.choice]
                else:
                    choice = results[int(input("Pick: "))]
            except IndexError:
                print("Invalid choice", file=sys.stderr)
                return 2
            except ValueError:
                print("Not a number", file=sys.stderr)
                return 3
        else:
            choice = results[0]
        if args.peerflix:
            process = Popen([find_executable("peerflix"), choice["download"], ("--" + env["PEERFLIX_PLAYER"] if env.get("PEERFLIX_PLAYER", None) else "")])
            process.wait()
        else:
            print(choice["download"], end="")
        return 0
    else:
        error_message = "({}) {}".format(
            query.get('error_code'),
            query.get('error', "Something weird happened")
        )
        print(error_message, file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
