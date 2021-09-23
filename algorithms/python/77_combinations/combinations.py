"""
77. combinations

组合
"""

from typing import List
import itertools


class Solution1:
    """
    Python 工具
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(itertools.combinations(range(1, n + 1), k))


class Solution2:
    """
    回溯法 + 剪枝
    """

    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = []
        ans = []

        def dfs(cur: int):
            # 剪枝，temp 的长度加上区间 [cur, n] 的小于 k，不可能构造出长度 k 的 temp
            if len(temp) + n - cur + 1 < k:
                return

            # 记录合法答案
            if len(temp) == k:
                ans.append(temp.copy())
                return

            # 考虑当前位置
            temp.append(cur)
            dfs(cur + 1)
            # 不考虑当前位置
            temp.pop()
            dfs(cur + 1)

        dfs(1)
        return ans
