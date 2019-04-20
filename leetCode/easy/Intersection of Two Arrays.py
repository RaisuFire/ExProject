class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = 0
        for i in range(len(s)):
            if s[i] == 'A':
                n += 1
                if n > 1:
                    return False
            if i < len(s) - 2 and s[i] == 'L' and s[i+1] == "L" and s[i+2] == "L":
                return False
        return True

if __name__ == "__main__":
    s = "PPALLL"
    so = Solution()
    c = so.checkRecord(s)
    print(c)