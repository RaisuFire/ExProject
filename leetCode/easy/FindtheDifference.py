class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        t_set = set(t)

        for i in t_set:
            print(t.count(i))
            if t.count(i) != s.count(i):
                return i

        return None

if __name__ == "__main__":
    s = "a"
    t = "aa"

    so = Solution()
    c = so.findTheDifference(s, t)
    # print(c)
