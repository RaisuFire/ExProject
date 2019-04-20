import json

from JsonParse import JsonParser


def test_is_valid():
    c = {"name": "John"}
    c1 = json.dumps(c)

    j1 = json.loads(c1)
    j2 = JsonParser.load(c1)

    print("j1", j1)
    print("j2", j2)
    assert j1 == j2


def test_parser():
    ...


if __name__ == "__main__":
    test_is_valid()