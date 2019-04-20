class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1:
            return 0
        a = list(set(s))
        d = {}
        for i in a:
            d[i] = 0
        for i in s:
            for k in d.keys():
                if i == k:
                    d[k] += 1
        print(d)

# i < len(s) - 1 and
if __name__ == "__main__":
    s = "leetcode"
    so = Solution()
    c = so.firstUniqChar(s)
    print(c)
