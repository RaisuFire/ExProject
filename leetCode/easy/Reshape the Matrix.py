class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        p = []
        for i in nums:
            for j in i:
                p.append(j)
        l = len(p)
        if l // r // c != 1:
            return nums

        ans = []
        index = 0
        for i in range(r):
            a = []
            for j in range(c):
                a.append(p[index])
                index += 1
            ans.append(a)
        return ans

"""
        if len(nums) * len(nums[0]) != (r * c):
            return nums
        
        result = []
        temp = []
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):

                temp.append(nums[i][j])
                count += 1
                if count == c:
                    result.append(temp)
                    temp = []
                    count = 0
            
        return result
"""


if __name__ == "__main__":
    nums = [[1, 2], [3, 4]]
    r = 1
    c = 4
    so = Solution()
    c = so.matrixReshape(nums, r, c)
    print(c)
