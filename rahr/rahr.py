#!/usr/bin/env python3
from requests import get
from argparse import ArgumentParser
import sys
from subprocess import Popen
from distutils.spawn import find_executable
from os import environ as env

def main():
    parser = ArgumentParser()
    parser.add_argument("search", nargs="+")
    parser.add_argument("--choice", type=int)
    parser.add_argument("--peerflix", help="If present, calls peerflix with the selected link. If env variable PEERFLIX_PLAYER is set, launches given player, otherwise video streams on <local ip>:8888", action="store_true")
    parser.add_argument("--jackett-host", help="Specify jackett host in form host:port. Defaults to localhost:9117. can also be provided with JACKETT_HOST", default=env.get("JACKETT_HOST", "localhost:9117"))
    parser.add_argument("--jackett-api-key", help="Specify jackett API key. can also be provided with JACKETT_API_KEY", default=env.get("JACKETT_API_KEY"))
    parser.add_argument("--jackett-indexer", help="Specify jackett indexer. Defaults to 'all'", default="all")
    args = parser.parse_args()
    if not args.jackett_api_key:
        print("Please provide jackett api key", file=sys.stderr)
        return 1
    query = get("http://{}/api/v2.0/indexers/{}/results".format(args.jackett_host, args.jackett_indexer), params={"apikey": args.jackett_api_key, "Query": " ".join(args.search)}).json()
    results = [r for r in query.get("Results") if r["Seeders"] > 0]
    results = sorted(results, key=lambda _: _["Grabs"])
    if results:
        for n,r in enumerate(results):
            print("{0}: {Title} ({CategoryDesc}) - S:{Seeders} P:{Peers} {Tracker}".format(n, **r), file=sys.stderr)
        if len(results) > 1:
            try:
                if args.choice is not None:
                    choice = results[args.choice]
                else:
                    print("Pick: ", file=sys.stderr)
                    choice = results[int(input())]
            except IndexError:
                print("Invalid choice", file=sys.stderr)
                return 2
            except ValueError:
                print("Not a number", file=sys.stderr)
                return 3
        else:
            choice = results[0]
        if args.peerflix:
            process = Popen([find_executable("peerflix"), choice["MagnetUri"] if choice["MagnetUri"] else choice["Link"], ("--" + env["PEERFLIX_PLAYER"] if env.get("PEERFLIX_PLAYER", None) else "")])
            process.wait()
        else:
            print(choice["MagnetUri"] if choice["MagnetUri"] else choice["Link"])
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
