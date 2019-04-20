class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        nums11 = nums1[:m]
        i, j, k = 0, 0, 0
        while k <= len(nums1):
            if i == m:
                nums1[k:] = nums2[j:]
                break
            if j == n:
                nums1[k:] = nums11[i:]
                break
            if nums11[i] > nums2[j]:
                nums1[k] = nums2[j]
                j += 1
                k += 1
            elif nums11[i] < nums2[j]:
                nums1[k] = nums11[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums11[i]
                nums1[k + 1] = nums2[j]
                j += 1
                i += 1
                k += 2
        return nums1


if __name__ == "__main__":
    nums1 = [0,0,3,0,0,0,0,0,0]
    nums2 = [-1,1,1,1,2,3]
    m = 3
    n = 6
    so = Solution()
    c = so.merge(nums1, m, nums2, n)
    print(c)
