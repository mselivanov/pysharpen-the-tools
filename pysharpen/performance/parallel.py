"""
Module demonstrates different performance improvement techniques
using parallelization means (threads, processes, asyncio)
"""
from urllib.request import urlopen
from collections import namedtuple
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import json
from timeit import timeit
import bz2
import sys


User = namedtuple("User", ["login", "name", "joined"])
logins = ("tebeka", "torvalds", "gvanrossum", "mselivanov")
with open(sys.argv[1], "rb") as fp:
    data = fp.read()
data_compressed = bz2.compress(data)
requests = [data_compressed]*40


def user_info(login_name):
    fp = urlopen("https://api.github.com/users/{login_name}".
                 format(login_name=login_name)).read().decode(encoding="utf-8")
    reply = json.loads(fp)
    joined = datetime.strptime(reply["created_at"], "%Y-%m-%dT%H:%M:%SZ")
    return User(login_name, reply["name"], joined)


def users_info(logins):
    return [user_info(login) for login in logins]


def users_info_threaded(logins):
    with ThreadPoolExecutor() as pool:
        return list(pool.map(user_info, logins))


def unpack(requests):
    return [bz2.decompress(request) for request in requests]


def unpack_proc(requests):
    with ProcessPoolExecutor() as pool:
        return list(pool.map(bz2.decompress, requests))


def test_threads():
    print("Non-threaded:",
          timeit("users_info(logins)",
                 "from __main__ import logins, User, users_info, user_info",
                 number=10))


def test_processes():
    print("Compression rate: {0}".format(len(data) / len(data_compressed)))
    print(bz2.decompress(data_compressed) == data)
    print("Single process:",
          timeit("unpack(requests)",
                 "from __main__ import requests, unpack",
                 number=1))
    print("Multi-process:",
          timeit("unpack_proc(requests)",
                 "from __main__ import requests, unpack_proc",
                 number=1))


# TODO: add asyncio example
def main():
    # test_threads()
    test_processes()


if __name__ == "__main__":
    main()
