class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        a = float('-inf')
        for i in range(len(A)):
            if A[i] > a:
                a = A[i]
        return A.index(a)


if __name__ == "__main__":
    s = [0,2,1,0]
    so = Solution()
    c = so.peakIndexInMountainArray(s)
    print(c)