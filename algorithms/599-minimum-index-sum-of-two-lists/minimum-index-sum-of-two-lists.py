"""
599. minimum-index-sum-of-two-lists

两个列表的最小索引总和
"""


import math
from typing import List


def find_restaurant(list1: List[str], list2: List[str]) -> List[str]:
    index = {v: k for k, v in enumerate(list1)}
    ans = []
    index_sum = math.inf
    for i, v in enumerate(list2):
        if v in index:
            j = index[v]
            if i + j < index_sum:
                index_sum = i + j
                ans = [v]
            elif i + j == index_sum:
                ans.append(v)

    return ans
