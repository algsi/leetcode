"""
547. number of provinces

https://leetcode.com/problems/number-of-provinces/
https://leetcode-cn.com/problems/number-of-provinces/

省份数量
"""

from typing import List


class Solution:
    """
    深度优先搜索
    """

    def find_circle_num(self, isConnected: List[List[int]]) -> int:
        def dfs(x: int):
            visited.add(x)
            for j in range(provinces):
                if isConnected[x][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)

        provinces = len(isConnected)
        visited = set()
        circles = 0

        for i in range(provinces):
            if i not in visited:
                dfs(i)
                circles += 1

        return circles
