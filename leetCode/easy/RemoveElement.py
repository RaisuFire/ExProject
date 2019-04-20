class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val not in nums:
            return len(nums)
        for x in nums:
            if val == x:
                nums.remove(val)
        self.removeElement(nums, val)
        return len(nums)


if __name__=='__main__':
    nums = [3, 3, 2, 2, 4]
    val = 3

    s = Solution()
    a = s.removeElement(nums, val)
    print(a)
