"""
136. Single Number

只出现一次的数字

https://leetcode.com/problems/single-number/
https://leetcode-cn.com/problems/single-number/

位运算技巧：异或操作，相同为1，相异为1
"""

from typing import List


def single_number(nums: List[int]) -> int:
    result = 0
    for num in nums:
        result ^= num

    return result
