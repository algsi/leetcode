"""
40. combination sum ii

组合总和 II
"""

from typing import List


class Solution:
    """
    搜索回溯 + 剪枝
    """

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []

        # 便于剪枝 & 便于去重
        candidates.sort()

        size = len(candidates)
        path = []
        ans = []

        def backtrack(begin: int, cur_target: int):
            if cur_target == 0:
                ans.append(path.copy())
                return

            for index in range(begin, size):
                if index > begin and candidates[index] == candidates[index - 1]:
                    # 解集不能包含重复的组合
                    continue

                residue = cur_target - candidates[index]
                if residue < 0:
                    break
                path.append(candidates[index])
                backtrack(index + 1, residue)
                path.pop()

        backtrack(0, target)
        return ans


def main():
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    solution = Solution()
    r = solution.combinationSum2(candidates, target)
    print(r)


if __name__ == '__main__':
    main()
