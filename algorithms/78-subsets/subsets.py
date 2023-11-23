"""
78. subsets

子集
"""

from typing import List


class Solution:
    """
    backtrack
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]  # 初始化空集
        n = len(nums)
        path = []

        def backtrack(begin: int, cur_size: int):
            if cur_size == 0:
                ans.append(path.copy())
                return

            for j in range(begin, n - cur_size + 1):
                path.append(nums[j])
                backtrack(j + 1, cur_size - 1)
                path.pop()

        for size in range(1, n + 1):
            # size 为子集元素个数
            for i in range(n - size + 1):
                # 剪枝
                path.append(nums[i])
                backtrack(i + 1, size - 1)
                path.pop()

        return ans


def main():
    nums = [1, 2, 3]
    solution = Solution()
    r = solution.subsets(nums)
    print(r)


if __name__ == '__main__':
    main()
