class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        sol = []
        while matrix:
            right = matrix[0]
            sol += right
            matrix = matrix[1:]
            if not matrix: return sol

            down = [i[-1] for i in matrix if i]
            sol += down
            matrix = [i[:-1] for i in matrix if i]
            if not matrix: return sol

            left = matrix[-1][::-1]
            sol += left
            matrix = matrix[:-1]
            if not matrix: return sol

            up = [i[0] for i in matrix if i][::-1]
            sol += up
            matrix = [i[1:] for i in matrix if i]
        return sol

if __name__ == "__main__":
    # nums = [[1, 2, 3, 4],
    #         [5, 6, 7, 8],
    #         [9, 10, 11, 12],
    #         [13, 14, 15, 16]]
    nums = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
    # nums = [[1, 2, 3, 4],
    #         [5, 6, 7, 8],
    #         [9, 10, 11, 12]]
    so = Solution()
    c = so.spiralOrder(nums)
    print(c)
