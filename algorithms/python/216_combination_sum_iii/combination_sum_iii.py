"""
216. combination sum iii

组合总和 III
"""

from typing import List


class Solution:
    """
    回溯搜索
    """

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def dfs(begin: int, target: int):
            """
            DFS需要保证path中的元素个数最多为 k 个

            :param begin: the begin number (inclusive)
            :param target: current target
            """
            size = len(path)
            if size == k and target == 0:
                ans.append(path.copy())
            if size >= k or target <= 0:
                return

            for index in range(begin, 10):
                if index > target:
                    # 剪枝
                    break
                path.append(index)
                dfs(index + 1, target - index)
                path.pop()

        dfs(1, n)
        return ans


def main():
    k, n = 3, 9
    solution = Solution()
    r = solution.combinationSum3(k, n)
    print(r)


if __name__ == '__main__':
    main()
