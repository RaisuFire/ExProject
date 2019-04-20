from math import sqrt


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # y = x/2
        # up = x
        # low = 0
        # count = 0
        # while abs(y * y - x) > 0.01:
        #     count += 1
        #     print(count)
        #     if y * y > x:
        #         up = y
        #         y = low + (y-low)/2
        #     else:
        #         low = y
        #         y = up - (up - y)/2
        # c = int(y)
        c = int(sqrt(x))
        return c

if __name__== "__main__":
    so = Solution()
    x = 10
    y = so.mySqrt(x)
    print(y)
