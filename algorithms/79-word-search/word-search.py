"""
79. word search

单词搜索
"""

from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    """
    回溯
    """
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def check(i: int, j: int, k: int) -> bool:
        """
        设函数 check(i, j, k) 表示判断以网格的 (i,j) 位置出发，能否搜索到单词 word[k..]
        """
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True
        visited.add((i, j))
        result = False
        for di, dj in directions:
            new_i, new_j = i + di, j + dj
            if 0 <= new_i < len(board) and 0 <= new_j < len(board[0]):
                if (new_i, new_j) not in visited:
                    if check(new_i, new_j, k + 1):
                        result = True
                        return result
        visited.remove((i, j))
        return result

    visited = set()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if check(i, j, 0):
                return True
    return False
