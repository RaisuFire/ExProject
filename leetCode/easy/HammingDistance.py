class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        c = 0
        a = x ^ y
        s = str(bin(a))
        for i in s:
            if i == '1':
                c += 1
        return c


if __name__ == "__main__":
    a = 1
    b = 4
    c = a ^ b
    so = Solution()
    c = so.hammingDistance(b, a)
    print(c)

