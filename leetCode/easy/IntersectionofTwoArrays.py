class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inums = []
        for i in nums1:
            if i in nums2 and i not in inums:
                inums.append(i)
        return inums


if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    so = Solution()
    c = so.intersection(nums1, nums2)
    print(c)