"""
1431. kids with the greatest number of candies

拥有最多糖果的孩子
"""

from typing import List


def kids_with_candies(candies: List[int], extraCandies: int) -> List[bool]:
    # 找出拥有的糖果数量中最大值
    target = max(candies)

    res = []
    for candy in candies:
        if candy + extraCandies >= target:
            res.append(True)
        else:
            res.append(False)

    return res
