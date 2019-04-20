class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        sortnums = sorted(nums)
        fb, sb = sortnums[-1], sortnums[-2]
        if fb < sb * 2:
            return -1
        else:
            for i in range(len(nums)):
                if fb == nums[i]:
                    return i


if __name__=="__main__":
    nums = [1]
    so = Solution()
    c = so.dominantIndex(nums)
    print(c)