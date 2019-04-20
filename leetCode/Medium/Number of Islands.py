class Solution(object):
    def isLand(self, row, col, grid):
        if grid[row][col] == "1":
            grid[row][col] = "0"
            self.isLand(row - 1, col, grid) if row > 0 else None
            self.isLand(row + 1, col, grid) if row < len(grid) - 1 else None
            self.isLand(row, col - 1, grid) if col > 0 else None
            self.isLand(row, col + 1, grid) if col < len(grid[0]) - 1 else None
            return True
        return False

    def numIslands(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.isLand(i, j, grid):
                    count += 1
        return count


if __name__ == "__main__":
    nums = [['1', '1', '1', '1', '0'],
            ['1', '1', '0', '1', '0'],
            ['1', '1', '0', '0', '0'],
            ['0', '0', '0', '0', '0']]
    so = Solution()
    c = so.numIslands(nums)
    print(c)
