"""
485. max consecutive ones

https://leetcode.com/problems/max-consecutive-ones/
https://leetcode-cn.com/problems/max-consecutive-ones/

最大连续 1 的个数
"""
from typing import List


def find_max_consecutive_ones(nums: List[int]) -> int:
    max_count = count = 0
    for num in nums:
        if num == 1:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    max_count = max(max_count, count)
    return max_count
