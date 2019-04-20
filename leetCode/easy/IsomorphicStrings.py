class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictst = {}
        dictts = {}
        for i in range(len(s)):
            dictst[s[i]] = t[i]
            dictts[t[i]] = s[i]
        t1 = ''
        s1 = ''
        for i in range(len(s)):
            t1 += dictst[s[i]]
            s1 += dictts[t[i]]
        return t1 == t and s1 == s

if __name__ == "__main__":
    s = "ab"
    t = "aa"
    so = Solution()
    c = so.isIsomorphic(s, t)
    print(c)
