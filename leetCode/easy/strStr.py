class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            if needle is None:
                return 0
            else:
                return haystack.index(needle)
        except:
            return -1


if __name__ == '__main__':
    str1 = "hello"
    str2 = "lll"

    s = Solution()
    print(s.strStr(str1, str2))

