from copy import deepcopy


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        c = deepcopy(matrix)

        for i in range(len(matrix)):
            matrix[i] = [c[j][i] for j in range(len(c[i]))][::-1]

"""
        matrix.reverse()
        r = len(matrix)
        for i in range(r):
            for j in range(i+1, r):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return 
"""

if __name__ == "__main__":
    nums1 = [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ]
    so = Solution()
    c = so.rotate(nums1)
    print(c)
