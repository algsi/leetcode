"""
47. permutation ii

全排列 Ⅱ
"""

from typing import List


class Solution:
    """
    backtrack 搜索回溯
    """

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def backtrack(k: int):
            """
            产生 list[k, n] 的所有排列
            """
            if k == n:
                ans.append(nums.copy())
                return

            # 存储本次递归交换过的元素
            record = set()
            for i in range(k, n):
                if nums[i] in record:
                    continue
                record.add(nums[i])
                nums[k], nums[i] = nums[i], nums[k]
                backtrack(k + 1)
                # 复原
                nums[k], nums[i] = nums[i], nums[k]

        backtrack(0)
        return ans


def main():
    nums = [1, 1, 2]
    solution = Solution()
    ans = solution.permuteUnique(nums)
    print(ans)


if __name__ == '__main__':
    main()
