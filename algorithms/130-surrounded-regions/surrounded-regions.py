"""
130. surrounded regions

被围绕的区域
"""

from typing import List

"""
注意到题目解释中提到：任何边界上的 O 都不会被填充为 X。 我们可以想到，所有的不被包围的 O 都直接或间接与边界上的 O 相连。我们可以利用这个性质判断 O 是否在边界上，具体地说：

对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；
最后我们遍历这个矩阵，对于每一个字母：
1. 如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
2. 如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X。


DFS or BFS
"""


class Solution:
    """
    DFS
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) <= 1:
            return

        # 对边界做 DFS
        row, col = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < row or not 0 <= y < col or board[x][y] != 'O':
                return

            board[x][y] = '#'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(row):
            dfs(i, 0)
            dfs(i, col - 1)
        for i in range(col - 1):
            dfs(0, i)
            dfs(row - 1, i)

        for i in range(row):
            for j in range(col):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'


if __name__ == "__main__":
    param = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    solution = Solution()
    solution.solve(param)
    print(param)
