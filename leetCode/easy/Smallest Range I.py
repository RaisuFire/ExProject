class Solution(object):
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        c = sorted(A)
        a = (c[-1] - c[0]) - 2 * K
        if a > 0:
            return a
        else:
            return 0


if __name__ == "__main__":
    A = [2, 7, 2]
    K = 1
    so = Solution()
    c = so.smallestRangeI(A, K)
    print(c)
