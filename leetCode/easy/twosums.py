class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # self.nums = nums
        # self.target = target
        a = len(nums)
        for x in range(a):
            for y in range(x+1, a):
                if (target == nums[x] + nums[y]):
                    return [x, y]

print(Solution.twoSum(object, [3,2,4], 6))

