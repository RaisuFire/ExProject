import math


class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        x = int(math.sqrt(c)) + 1
        for i in range(x):
            b = c - i * i
            xb = math.sqrt(b)
            # return True if xb == int(xb) else False
            if xb == int(xb):
                return True
        return False


if __name__ == '__main__':
    c = 2
    s = Solution()
    x = s.judgeSquareSum(c)
    print(x)
