"""
888. fair candy swap

https://leetcode.com/problems/fair-candy-swap/
https://leetcode-cn.com/problems/fair-candy-swap/

公平的糖果棒交换
"""

from typing import List


def fair_candy_swap(A: List[int], B: List[int]) -> List[int]:
    sum_A = sum(A)
    sum_B = sum(B)
    delta = (sum_A - sum_B) // 2
    rec = set(A)

    for y in B:
        x = y + delta
        if x in rec:
            return [x, y]
