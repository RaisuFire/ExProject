class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = nums.count(0)
        for i in range(n):
            nums.append(0)
            nums.remove(0)
        return nums

if __name__ == "__main__":
    a = [0, 1, 0, 3, 12]
    so = Solution()
    d = so.moveZeroes(a)
    print(d)


"""
        r=0
        count=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[r]=nums[i]
                r+=1
            else:
                count+=1
                
        for j in range(count):
            nums[len(nums)-1-j]=0
            
"""