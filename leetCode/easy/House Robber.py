class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        notrob = 0
        for i in range(len(nums)):
            print("notrob", notrob)
            print("rob", rob)
            currob = notrob + nums[i]
            notrob = max(notrob, rob)
            rob = currob
        return max(rob, notrob)


if __name__ == "__main__":
    nums = [2, 7, 9, 3, 1]
    so = Solution()
    c = so.rob(nums)
    print(c)