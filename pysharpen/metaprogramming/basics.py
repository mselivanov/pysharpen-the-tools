from collections.abc import MutableSequence
from collections.abc import Mapping
import inspect
import unittest
import requests
import warnings
import os
import shelve
import json

JSON_FILE = "test_data.json"
URL = "https://www.oreilly.com/pub/sc/osconfeed"

def load():
    if not os.path.exists(JSON_FILE):
        msg = f"Loading {JSON_FILE} from {URL}"
        warnings.warn(msg)
        resp = requests.get(URL)
        with open(JSON_FILE, "wt", encoding="utf-8") as local_file:
            local_file.write(resp.text)
    with open(JSON_FILE, "rt", encoding="utf-8") as local_file:
        return json.load(local_file)


class AttributeDict:
    def __new__(cls, arg):
        "Create attribute dict element"
        if isinstance(arg, Mapping):
            return super().__new__(cls)
        elif isinstance(arg, MutableSequence):
            return [cls(elem) for elem in arg]
        else:
            return arg

    def __init__(self, data):
        self._data = dict(data)

    def __getattr__(self, name):
        if hasattr(self._data, name):
            return getattr(self._data, name)
        else:
            return AttributeDict(self._data[name])


DB_NAME = "conference2.db"
CONFERENCE = "conference.115"


class MissignDatabaseError(RuntimeError):
    "Raise when database is required but isn't set"


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class DbRecord(Record):
    __db = None

    @staticmethod
    def set_db(db):
        DbRecord.__db = db

    @staticmethod
    def get_db():
        return DbRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = f"db is not set. call {cls.__name__}.set_db(my_db)"
                raise MissignDatabaseError(msg)
            else:
                raise

    def __repr__(self):
        if hasattr(self, "serial"):
            cls_name = self.__class__.__name__
            return f"<{cls_name} serial={self.serial!r}>"
        else:
            return super().__repr__()


class Event(DbRecord):
    @property
    def venue(self):
        key = f"venue.{self.venue_serial}"
        return self.__class__.fetch(key)

    @property
    def speakers(self):
        if not hasattr(self, "_speaker_objs"):
            spkr_serials = self.__dict__["speakers"]
            fetch = self.__class__.fetch
            self._speaker_objs = [
                fetch(f"speaker.{key}") for key in spkr_serials
            ]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, "name"):
            cls_name = self.__class__.__name__
            return f"<{cls_name} {self.name!r}>"
        else:
            return super().__repr__()


def load_db(db):
    raw_data = load()
    for collection, rec_list in raw_data["Schedule"].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DbRecord)
        if inspect.isclass(cls) and issubclass(cls, DbRecord):
            factory = cls
        else:
            factory = DbRecord
        for record in rec_list:
            key = f"{record_type}.{record['serial']}"
            record["serial"] = key
            db[key] = factory(**record)


class AttributeDictTest(unittest.TestCase):
    def test_simple_attribute_access(self):
        "Test first level attribute access"
        d = {"a": 1, "b": "Hello"}
        ad = AttributeDict(d)
        self.assertEqual(ad.a, 1)
        self.assertEqual(ad.b, "Hello")

    def test_list_access(self):
        "Test first level attribute access"
        d = {"a": 1, "b": "Hello", "c": [{"cinner": 2}]}
        ad = AttributeDict(d)
        self.assertEqual(ad.a, 1)
        self.assertEqual(ad.b, "Hello")
        self.assertEqual(ad.c[0].cinner, 2)


def main():
    db = shelve.open(DB_NAME)
    if CONFERENCE not in db:
        load_db(db)
    DbRecord.set_db(db) 
    event = DbRecord.fetch("event.33950")
    print(event)
    print(event.venue)
    for spkr in event.speakers:
        print(f"{spkr.serial} {spkr.name}")


if __name__ == "__main__":
    # unittest.main()
    main()
