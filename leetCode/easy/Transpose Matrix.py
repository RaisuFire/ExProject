class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ans = []
        for i in range(len(A[0])):
            k = []
            for j in range(len(A)):
                k.append(A[j][i])
            ans.append(k)
        return ans



if __name__ == "__main__":
    # A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    A = [[1, 2, 3], [4, 5, 6]]
    so = Solution()
    c = so.transpose(A)
    print(c)