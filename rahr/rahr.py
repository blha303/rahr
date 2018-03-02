#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser
import sys

token = get("https://torrentapi.org/pubapi_v2.php?get_token=get_token").json()["token"]

def main():
    parser = ArgumentParser()
    parser.add_argument("search", nargs="+")
    parser.add_argument("--choice", type=int)
    args = parser.parse_args()
    results = get("https://torrentapi.org/pubapi_v2.php", params={"mode": "search", "search_string": " ".join(args.search), "token": token, "format": "json"}).json()["torrent_results"]
    if results:
        for n,r in enumerate(results):
            print("{}: {} ({})".format(n, r["filename"], r["category"]), file=sys.stderr)
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
        print(r["download"], end="")
        return 0
    else:
        print("No results", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
