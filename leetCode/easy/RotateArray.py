class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            last = nums.pop()
            nums.insert(0, last)
        return nums

if __name__ == "__main__":
    nums = [-1,-100,3,99]
    k = 2
    so = Solution()
    c = so.rotate(nums, k)
    print(c)