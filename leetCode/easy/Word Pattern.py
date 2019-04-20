from collections import defaultdict


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # def removelm(p, v):
        #     n = []
        #     for i in p:
        #         if i == v:
        #             n.append(i)
        #     for i in n:
        #         p.remove(i)
        #
        # d = {}
        # p = []
        # for i in pattern:
        #     p.append(i)
        # s = str.split()
        #
        # if len(p) != len(s):
        #     return False
        #
        # for i in range(len(p)):
        #     d[p[i]] = s[i]
        #
        # for k, v in d.items():
        #     if k in p:
        #         removelm(p, k)
        #         removelm(s, v)
        #         if len(p) == 0 or len(s) == 0:
        #             break
        #
        # if len(p) > 0 or len(s) > 0:
        #     return False
        # else:
        #     return True

        words = str.split()

        if len(pattern) != len(words):
            return False

        dic1 = defaultdict(int)
        dic2 = defaultdict(int)

        for i in range(len(pattern)):
            print(i, dic1[pattern[i]], dic2[words[i]])
            if dic1[pattern[i]] != dic2[words[i]]:
                return False
            dic1[pattern[i]] = i + 1
            dic2[words[i]] = i + 1

        return True


if __name__ == '__main__':
    pattern = "abba"
    stp = "dog dog dog dog"
    so = Solution()
    c = so.wordPattern(pattern, stp)

"""
        words = str.split()
        
        if len(pattern) != len(words):
            return False
        
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        
        for i in range(len(pattern)):
            if dic1[pattern[i]] != dic2[words[i]]:
                return False
            dic1[pattern[i]] = i+1
            dic2[words[i]] = i+1
        
        return True
"""

