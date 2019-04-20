import string


class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        le = list(string.ascii_uppercase)
        dictl = {}
        n = 1
        for i in le:
            dictl[i] = n
            n += 1

        ans = 0
        for i in range(len(s)):
            ans += dictl[s[i]] * 26 ** (len(s) - i - 1)
        return ans


if __name__ == "__main__":
    input = "ZY"
    so = Solution()
    c = so.titleToNumber(input)
    print(c)
