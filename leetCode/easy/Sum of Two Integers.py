class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        ba = bin(a)
        bb = bin(b)
        print(a ^ b)
        # ans = ba & bb
        # return ans


if __name__ == "__main__":
    a = 1
    b = 2
    so = Solution()
    c = so.getSum(a, b)
    print(c)
