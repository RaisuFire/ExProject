class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']

        for ch in S:
            if ch.isalpha():
                print(res)
                res = [i + j for i in res for j in [ch.upper(), ch.lower()]]
            else:
                res = [i + ch for i in res]
        return res


if __name__ == "__main__":
    s = "mQe"
    so = Solution()
    c = so.letterCasePermutation(s)
    print(c)
