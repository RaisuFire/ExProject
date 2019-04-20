
class Solution(object):
    def isValid(self, s):
        parens = "(){}[]"
        open_brackets = '({['
        opposite = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        lists = []
        for pr in s:
            try:
                if pr in open_brackets:
                    lists.append(pr)
                elif lists.pop() != opposite[pr]:
                    return False
                else:
                    pass
            except Exception as e:
                return False
        if len(lists):
            return False
        else:
            return True


if __name__ == "__main__":
    s = "()"
    solu = Solution()
    x = solu.isValid(s)
    print(x)
