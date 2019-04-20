class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        for i in range(len(nums)):
            val = abs(nums[i]) - 1
            if nums[val] > 0:
                nums[val] = -nums[val]

        for i in range(len(nums)):
            if nums[i] > 0:
                ret.append(i+1)
        return ret

if __name__ == "__main__":
    a = [4, 3, 2, 7, 8, 2, 3, 1]
    so = Solution()
    c = so.findDisappearedNumbers(a)
    print(c)