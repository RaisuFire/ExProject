from JsonParse import (
    token_null,
    Token,
    TypeJson,
    token_boolean,
    token_number, token_string, token_symbol)


def test_token_null():
    json_text = 'null'
    i, token = token_null(json_text, i=0)
    assert i == 4
    assert token.type == TypeJson.LeptNull
    assert token.value is None


def test_token_true():
    json_text = 'true'
    i, token = token_boolean(json_text, i=0)
    assert i == 4
    assert token.type == TypeJson.LeptBoolean
    assert token.value is True


def test_token_false():
    json_text = 'false'
    i, token = token_boolean(json_text, i=0)
    assert i == 5
    assert token.type == TypeJson.LeptBoolean
    assert token.value is False


def test_token_number():
    json_text = '123456'
    i, token = token_number(json_text, i=0)
    assert i == len(json_text)
    assert token.type == TypeJson.LeptNumber
    assert token.value == str(123456)


def test_token_string():
    json_text = 'sdf546'
    i, token = token_string(json_text, i=0)
    assert i == len(json_text)
    assert token.type == TypeJson.LeptString
    assert token.value == "sdf546"


def test_token_separator():
    json_text = '{'
    i, tokensymbol = token_symbol(json_text, i=0)


def test_token():
    # test_token_null()
    # test_token_true()
    # test_token_false()
    # test_token_number()
    # test_token_string()
    test_token_separator()


if __name__ == "__main__":
    test_token()
