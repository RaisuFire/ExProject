class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        c = 0
        if 2**c == n:
            return True
        while 2**c < n:
            c += 1
            if 2**c == n:
                return True
        return False


if __name__ == "__main__":
    n = 218
    so = Solution()
    c = so.isPowerOfTwo(n)
    print(c)