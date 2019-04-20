class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if target > nums[i]:
                continue
            elif target == nums[i]:
                return i
            elif target < nums[i]:
                return i
        return len(nums)



if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 7
    s = Solution()
    x = s.searchInsert(nums, target)
    print(x)
