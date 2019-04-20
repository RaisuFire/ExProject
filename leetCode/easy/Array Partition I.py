class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = sorted(nums)
        # l = filter(lambda x: x % 2 == 0, range(len(nums)))
        # ans = sum(nums[i] for i in l)
        # return ans

        nums = sorted(nums)
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]
        return sum

if __name__ == '__main__':
    nums = [1, 1, 1, 1]
    so = Solution()
    print(so.arrayPairSum(nums))
