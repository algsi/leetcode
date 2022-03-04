"""
200. number of islands

岛屿数量
"""

from typing import List


class Solution:
    def num_is_lands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0:
            return 0

        # 标记，注意二维数组的生成方式
        flag: List[List[bool]] = [[False] * len(grid[0]) for _ in range(len(grid))]
        num = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # 当前节点是岛屿并且还没有被遍历
                if grid[i][j] == "1" and not flag[i][j]:
                    num += 1
                    self.depth_first_search(grid, flag, i, j)

        return num

    def depth_first_search(self, grid: List[List[str]], flag: List[List[bool]], i: int, j: int):
        """
        深度优先搜索
        """
        if flag[i][j]:
            # 当前节点已经被遍历
            return
        else:
            # 标记当前节点已经被遍历
            flag[i][j] = True

        # 当前岛屿的左边也是岛屿并且还没有被遍历时
        if j > 0 and grid[i][j - 1] == "1" and not flag[i][j - 1]:
            self.depth_first_search(grid, flag, i, j - 1)

        # 当前岛屿的右边也是岛屿并且还没有被遍历时
        if j < len(grid[i]) - 1 and grid[i][j + 1] == "1" and not flag[i][j + 1]:
            self.depth_first_search(grid, flag, i, j + 1)

        # 当前岛屿的上边也是岛屿并且还没有被遍历时
        if i > 0 and grid[i - 1][j] == "1" and not flag[i - 1][j]:
            self.depth_first_search(grid, flag, i - 1, j)

        # 当前岛屿的下边也是岛屿并且还没有被遍历时
        if i < len(grid) - 1 and grid[i + 1][j] == "1" and not flag[i + 1][j]:
            self.depth_first_search(grid, flag, i + 1, j)
