class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        minum = min(nums)
        ret = 0
        for i in nums:
            ret += i - minum
        return ret

