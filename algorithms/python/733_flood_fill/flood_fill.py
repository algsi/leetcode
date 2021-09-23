"""
733. flood fill

图像渲染
"""

from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        DFS
        """
        if image is None:
            return image

        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        rows, cols = len(image), len(image[0])

        def dfs(row: int, col: int):
            if 0 <= row < rows and 0 <= col < cols and image[row][col] == old_color:
                image[row][col] = newColor
                for x_d, y_d in directs:
                    dfs(row + x_d, col + y_d)

        dfs(sr, sc)
        return image
