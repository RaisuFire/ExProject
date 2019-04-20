class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        num = abs(num)
        while num > 1:
            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num /5
            else:
                return False
        return True


if __name__ == "__main__":
    num = -1000
    so = Solution()
    print(so.isUgly(num))

