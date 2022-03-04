"""
645. set mismatch

https://leetcode.com/problems/set-mismatch/
https://leetcode-cn.com/problems/set-mismatch/

错误的集合
"""

import collections
from typing import List


def find_error_nums_v1(nums: List[int]) -> List[int]:
    """
    哈希表
    """
    length = len(nums)
    counter = collections.Counter(nums)
    ans = [0] * 2
    for i in range(1, length + 1):
        if counter[i] == 2:
            ans[0] = i
        elif counter[i] == 0:
            ans[1] = i
    return ans


def find_error_nums_v2(nums: List[int]) -> List[int]:
    """
    数学方法
    """
    length = len(nums)
    total = sum(set(nums))
    return [sum(nums) - total, (length + 1) * length // 2 - total]
