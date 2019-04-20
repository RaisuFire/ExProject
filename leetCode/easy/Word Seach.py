class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        row = len(board)
        if row == 0:
            return False
        col = len(board[0])
        for i in range(0, row):
            for j in range(0, col):
                if self.dfs(i, j, board, word[0:]):
                    return True
        return False

    def dfs(self, row, col, board, word):
        if len(word) == 0:
            return True
        if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]):
            return False
        if board[row][col] != '#' and board[row][col] == word[0]:
            tmp = board[row][col]
            board[row][col] = '#'
            if self.dfs(row - 1, col, board, word[1:]) or self.dfs(row + 1, col, board, word[1:]) \
                or self.dfs(row, col - 1, board, word[1:]) or self.dfs(row, col + 1, board, word[1:]):

                return True
            else:
                board[row][col] = tmp

        return False


if __name__ == "__main__":
    word = "ABCCED"
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    so = Solution()
    c = so.exist(board, word)
    print(c)
