"""
LeetCode 187：重复的DNA序列

https://leetcode-cn.com/problems/repeated-dna-sequences/
"""

from typing import Set


def find_repeated_dna_sequences(s: str) -> Set[str]:
    """
    方法一：线性时间窗口切片 + HashSet
    """
    l, n = 10, len(s)
    seen, output = set(), set()

    for start in range(n - l + 1):
        tmp = s[start:start + l]
        if tmp in seen:
            output.add(tmp)
        else:
            seen.add(tmp)

        return output
