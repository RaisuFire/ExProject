def testrevices(n, t):
    if n is None and t is None:
        return True
    elif n is None and t is not None:
        return False
    elif n is not None and t is None:
        return False
    else:
        if n[-1] != t[-1]:
            n = n [:-1]
            return testrevices(n, t)
        else:
            return True

if __name__ == "__main__":
    n = [1, 2, 3, 4]
    t = [1, 2]
    print(testrevices(n, t))

