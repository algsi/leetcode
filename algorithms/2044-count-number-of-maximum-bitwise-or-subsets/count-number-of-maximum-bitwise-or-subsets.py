"""
2044. count-number-of-maximum-bitwise-or-subsets

统计按位或能得到最大值的子集数目
"""

from typing import List


def count_max_or_subsets(nums: List[int]) -> int:
    """
    回溯
    """
    max_or, cnt = 0, 0

    def dfs(pos: int, or_val: int) -> None:
        if pos == len(nums):
            nonlocal max_or, cnt
            if or_val > max_or:
                max_or, cnt = or_val, 1
            elif or_val == max_or:
                cnt += 1
            return
        dfs(pos + 1, or_val | nums[pos])
        dfs(pos + 1, or_val)

    dfs(0, 0)
    return cnt
