class Solution(object):
    def search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # print(left,right,mid)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1

    # def search(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: int
    #     """
    #     def searchval(nums, target):
    #         l = 0
    #         h = len(nums) - 1
    #         while l <= h:
    #             m = int((l + h) / 2)
    #             if target == nums[m]:
    #                 return target
    #             elif target > nums[m]:
    #                 l = m + 1
    #                 return searchval(nums[l:], target)
    #             else:
    #                 h = m - 1
    #                 return searchval(nums[:h+1], target)
    #         return None
    #     a = searchval(nums, target)
    #     print(a)
    #     if a is None:
    #         return -1
    #     else:
    #         return nums.index(a)


if __name__ == '__main__':
    nums = [-1,0,5]
    target = -1
    so =Solution()
    c = so.search(nums, target)
    print(c)

