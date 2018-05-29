from passlib.hash import sha256_crypt as sha256
import timeit
from functools import lru_cache


salt = "Qazwsx123fjhvnn"


users = {
        sha256.using(rounds=5000).hash("bugs"): "bunny",
        sha256.using(rounds=5000).hash("duffy"): "duck",
        sha256.using(rounds=5000).hash("elmer"): "cat"
        }


def user_from_key(key):
    key_enc = sha256.using(rounds=5000, salt=salt).hash("bugs")
    return users.get(key_enc)


@lru_cache(maxsize=1024)
def user_from_key_cached(key):
    key_enc = sha256.using(rounds=5000, salt=salt).hash("bugs")
    return users.get(key_enc)


# TODO: Add joblib example
def test_crypt():
    print("Crypt without cache: {0}".format(
        timeit.timeit("user_from_key('bugs')",
                      "from __main__ import user_from_key, salt",
                      number=100)))
    print("Crypt with cache: {0}".format(
        timeit.timeit("user_from_key_cached('bugs')",
                      "from __main__ import user_from_key_cached, salt",
                      number=100)))


if __name__ == "__main__":
    test_crypt()
