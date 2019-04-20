class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return str.lower()


if __name__=="__main__":
    a = "Hello"
    so = Solution()
    print(so.toLowerCase(a))