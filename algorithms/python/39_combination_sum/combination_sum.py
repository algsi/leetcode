"""
39. combination sum

组合总和
"""
from typing import List


class Solution:
    """
    搜索回溯
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        size = len(candidates)

        # 剪枝
        candidates.sort()

        # 在遍历的时候记录路径，这是一个栈
        path = []
        ans = []

        def dfs(begin: int, cur_target: int):
            """
            DFS

            :param begin: the beginning element
            :param cur_target: current target
            """

            if cur_target == 0:
                # 记录当前解
                ans.append(path.copy())
                return

            for index in range(begin, size):
                residue = cur_target - candidates[index]
                if residue < 0:
                    # 因为经过排序，所以这里可以直接 break 剪枝，而不是 continue
                    break
                path.append(candidates[index])
                dfs(begin, residue)
                path.pop()

        dfs(0, target)
        return ans
