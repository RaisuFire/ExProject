class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        # c = []
        # d = []
        # for a in A:
        #     if a % 2 == 0:
        #         c.append(a)
        #     else:
        #         d.append(a)
        # ans = []
        # for i in c:
        #     ans.append(i)
        # for i in d:
        #     ans.append(i)
        # return ans
        ans = []
        for a in A:
            if a % 2 == 0:
                ans.insert(0, a)
            else:
                ans.append(a)
        return ans


if __name__ == "__main__":
    s = [3,1,2,4]
    so = Solution()
    c = so.sortArrayByParity(s)
    print(c)