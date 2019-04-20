class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] < nums[i - 1]:
                return nums[i]


if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    so = Solution()
    c = so.findMin(nums)
    print(c)
