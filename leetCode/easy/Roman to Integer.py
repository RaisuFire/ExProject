class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictri = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans, i = 0, 0
        while i < len(s):
            if i <= len(s) - 2 and dictri[s[i]] < dictri[s[i + 1]]:
                ans += dictri[s[i + 1]] - dictri[s[i]]
                i += 2
            else:
                ans += dictri[s[i]]
                i += 1
        return ans


if __name__ == "__main__":
    str = "IV"
    so = Solution()
    x = so.romanToInt(str)
    print(x)
