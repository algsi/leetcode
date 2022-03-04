"""
785. is graph bipartite

https://leetcode.com/problems/is-graph-bipartite/
https://leetcode-cn.com/problems/is-graph-bipartite/

判断二分图
"""

from typing import List


class Solution:
    """
    DFS + 颜色标记
    """

    def isBipartite(self, graph: List[List[int]]) -> bool:
        UNCOLORED, RED, GREEN = 0, 1, 2

        n = len(graph)
        colors = [UNCOLORED] * n
        valid = True

        def dfs(node: int, color: int):
            nonlocal valid
            colors[node] = color
            cNei = (GREEN if color == RED else RED)
            for neighbor in graph[node]:
                if colors[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif colors[neighbor] != cNei:
                    valid = False
                    return

        for i in range(n):
            if colors[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    return False

        return valid


if __name__ == '__main__':
    g = [[2, 3, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [0, 1, 3, 4, 5, 6, 7, 8, 9], [0, 1, 2, 4, 5, 6, 7, 8, 9],
         [1, 2, 3, 6, 9], [0, 1, 2, 3, 7, 8, 9], [0, 1, 2, 3, 4, 7, 8, 9], [0, 1, 2, 3, 5, 6, 8, 9],
         [0, 1, 2, 3, 5, 6, 7], [0, 1, 2, 3, 4, 5, 6, 7]]
    solution = Solution()
    print(solution.isBipartite(g))
