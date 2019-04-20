class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        maxArea = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, self.helper(grid, i, j))
                    # maxArea = self.helper(grid, i, j)
        return maxArea

    def helper(self, grid, i, j):
        if len(grid) == 0:
            return 0
        if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[i]) and grid[i][j] == 1:
            grid[i][j] = 0  # to mark as visited
            return 1 + self.helper(grid, i + 1, j) + self.helper(grid, i - 1, j) + \
                   self.helper(grid, i, j - 1) + self.helper(grid, i, j + 1)
        return 0

if __name__ == "__main__":
    nums = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    so = Solution()
    c = so.maxAreaOfIsland(nums)
    print(c)
