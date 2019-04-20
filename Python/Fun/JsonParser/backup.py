from enum import Enum


class TypeJson(Enum):
    LeptNull = 0
    LeptFalse = 1
    LeptTrue = 2
    LeptNumber = 3
    LeptString = 4
    LeptArray = 5
    LeptObject = 6


class TypeSymbol(Enum):
    Colon = 0  #:
    Comma = 1  # ,
    BraceLeft = 2  # {
    BraceRight = 3  # }
    BracketLeft = 4  # [
    BracketRight = 5  # ]


class TypeAccess(Enum):
    Lept_Parse_Ok = 0
    LEPT_PARSE_EXPECT_VALUE = 1
    LEPT_PARSE_INVALID_VALUE = 2
    LEPT_PARSE_ROOT_NOT_SINGULAR = 3


class Token(object):
    def __init__(self, _type, value):
        self.type = _type
        self.value = value


def lept_parse(tokens, json):
    j = json.strip()




if __name__ == "__main__":
    lept_parse()

