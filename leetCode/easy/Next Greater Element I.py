class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        great_nums = []
        for num in findNums:
            n = nums.index(num)
            if n == len(nums) - 1:
                great_nums.append(-1)
            elif num > max(nums[n+1:]):
                great_nums.append(-1)
            else:
                for i in range(n, len(nums)):
                    if nums[i] > num:
                        great_nums.append(nums[i])
                        break
        return great_nums

"""
better solutation

        nums2=nums
        ht = {}
        st = []
        for item in nums2:
            while st!=[]:
                if st[-1]<item:
                    ht[st[-1]]=item
                    st=st[:-1]
                else:
                    break
            st.append(item)
        
        ans = []
        for item in findNums:
            if item in ht:
                ans.append(ht[item])
            else:
                ans.append(-1)
        return ans
"""
if __name__ == "__main__":
    # nums1 = [4,1,2]
    # nums2 = [1,3,4,2]
    # so = Solution()
    # a = so.nextGreaterElement(nums1, nums2)
    # print(a)

    a = [1, 3,5,6,]
    print(a[:-1])