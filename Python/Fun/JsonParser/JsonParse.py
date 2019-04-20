from enum import Enum


class TypeJson(Enum):
    LeptNull = 0
    LeptBoolean = 1
    LeptNumber = 2
    LeptString = 3
    LeptArray = 4
    LeptObject = 5


class TypeSymbol(Enum):
    Colon = 0  #:
    Comma = 1  # ,
    BraceLeft = 2  # {
    BraceRight = 3  # }
    BracketLeft = 4  # [
    BracketRight = 5  # ]


class Token():
    is_valid = True

    def __init__(self, _type, value):
        super(Token, self).__init__()
        self.type = _type
        self.value = value

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '{}\n{} \n'.format(classname, s)


class TokenSeparator(Token):
    is_valid = False

    _map = {
        ':': TypeSymbol.Colon,
        ',': TypeSymbol.Comma,
        '{': TypeSymbol.BraceLeft,
        '}': TypeSymbol.BraceRight,
        '[': TypeSymbol.BracketLeft,
        ']': TypeSymbol.BracketRight
    }

    def __init__(self, value):
        _type = self._map[value]
        super(TokenSeparator, self).__init__(_type, value)


def token_null(text, i):
    if text[i:i + 4] == 'null':
        token = Token(TypeJson.LeptNull, None)
        i += 4
        return i, token


def token_boolean(text, i):
    ch = text[i]
    if ch == 't':
        if text[i:i + 4] == 'true':
            token = Token(TypeJson.LeptBoolean, True)
            i += 4
            return i, token
    elif ch == 'f':
        if text[i:i + 5] == 'false':
            token = Token(TypeJson.LeptBoolean, False)
            i += 5
            return i, token


def token_number(text, i):
    num = ''
    num += text[i]
    i += 1
    while i < len(text) and text[i].isnumeric():
        num += text[i]
        i += 1
    token = Token(TypeJson.LeptNumber, num)
    return i, token


def token_string(text, i=0):
    str = ''
    offset = i + 1
    while offset < len(text):
        if text[offset] == '"':
            offset += 1
            break
        offset += 1

    str = text[i+1:offset-1]
    token = Token(TypeJson.LeptString, str)
    return offset, token


def token_symbol(text, i):
    ch = text[i]
    tokensymbol = TokenSeparator(ch)
    i += 1
    return i, tokensymbol


def json_tokens(text):
    tokens = []
    i = 0
    lenght = len(text) - 1
    while i < lenght:
        ch = text[i]
        if ch.isspace():
            i += 1
        elif ch == 'n':
            i, token = token_null(text, i)
            tokens.append(token)
        elif ch == 't' or ch == 'f':
            i, token = token_boolean(text, i)
            tokens.append(token)
        elif ch == '-' or ch.isnumeric():
            # 暂时不处理浮点数，科学计数法, 非实数，非10进制数
            i, token = token_number(text, i)
            tokens.append(token)
        elif ch == '"':
            # 为了省事不处理转义，原谅我！连Unicode也不支持，对不起！
            i, token = token_string(text, i)
            tokens.append(token)
        elif ch in ':,{}[]':
            i, token = token_symbol(text, i)
            tokens.append(token)
        else:
            raise ValueError('json tokens error')
    return tokens


class JsonParser():
    def __init__(self, tokens):
        self._tokens = tokens
        self._index = 0
        self._length = len(self._tokens)

    def cursor(self):
        return self._tokens[self._index]

    def _parser(self):
        tk = self.cursor()
        self._index += 1
        if tk is None:
            raise ValueError("token is invalid ")
        elif tk.is_valid is True:
            return tk.value
        elif tk.type == TypeSymbol.BraceLeft:
            return self._parse_object()
        elif tk.type == TypeSymbol.BracketLeft:
            return self._parse_array()
        else:
            raise ValueError("invalid token", tk)

    def _parse_object(self):
        data = {}
        tk = self.cursor()
        while self._index < self._length - 1:
            if tk.type == TypeJson.LeptString:
                k = tk.value
                self._index += 1
                nt = self.cursor()
                if nt.type == TypeSymbol.Colon:
                    self._index += 1
                    data[k] = self._parser()
                else:
                    raise ValueError("invalid json parse object")
            elif tk.type == TypeSymbol.Comma:
                self._index += 1
            elif tk.type == TypeSymbol.BraceRight:
                return data
            else:
                raise ValueError('parse error, invalid Token')
        return data

    def _parse_array(self):
        data = []
        while self._index < self._length - 1:
            tk = self.cursor()
            if tk.type == TypeSymbol.BracketRight:
                return data
            elif tk.type == TypeSymbol.Comma:
                self._index += 1
            else:
                d = self._parser()
                data.append(d)
        return data

    @classmethod
    def parse(cls, tokens):
        m = cls(tokens)._parser()
        return m

    @classmethod
    def load(cls, text):
        tokens = json_tokens(text)
        data = cls.parse(tokens)
        return data


if __name__ == "__main__":
    text = '"sdf534"'
    result = json_tokens(text)
