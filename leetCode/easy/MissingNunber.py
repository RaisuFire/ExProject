class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = sorted(nums)

        for i in range(len(ns)):
            if i != ns[i]:
                return i
        return ns[len(ns) - 1] + 1

if __name__ == "__main__":
    nums = [0]
    so = Solution()
    c = so.missingNumber(nums)
    print(c)

