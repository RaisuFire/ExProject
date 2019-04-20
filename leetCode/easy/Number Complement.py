from math import sqrt


class Solution:
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        a = ''
        c = bin(num).split('b')[1]
        for i in c:
            if i == str(0):
                a += str(1)
            else:
                a += str(0)
        ans = int(a, 2)
        return ans

"""
这种没人用的东西懒得看
        n = 1
        while n <= num:
            n <<= 1
        return (n-1)^num
"""


if __name__ == "__main__":
    n = 5
    so = Solution()
    c = so.findComplement(n)
    print(c)
