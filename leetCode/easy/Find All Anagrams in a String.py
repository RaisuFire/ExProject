from typing import Counter

from pylint.test.input.func_w0612 import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        n, m = len(s), len(p)
        if n < m: return res
        phash, shash = [0] * 123, [0] * 123
        for x in p:
            phash[ord(x)] += 1
            print("phash", phash)
        for x in s[:m - 1]:
            shash[ord(x)] += 1
            print("sh111", shash)
        for i in range(m - 1, n):
            shash[ord(s[i])] += 1
            print("shash", shash)
            if i - m >= 0:
                shash[ord(s[i - m])] -= 1
            if shash == phash:
                res.append(i - m + 1)
        return res


if __name__ == "__main__":
    s = "abab"
    p = "ab"
    so = Solution()
    c = so.findAnagrams(s, p)
    print(c)
