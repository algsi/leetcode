from math import inf
from typing import List


def find_longest_chain(pairs: List[List[int]]) -> int:
    """
    贪心算法：
    要挑选最长数对链的第一个数对时，最优的选择就是挑选第二个数字最小的，这样能给挑选后续数对留下更多的空间。
    挑完第一个数对后，要挑第二个数对时，也按照相同的思路，是在剩下的数对中，第一个数字满足题意的条件下，挑选第二个数字最小的。
    """
    new_pairs = sorted(pairs, key=lambda p: p[1])
    cur, res = -inf, 0
    for x, y in new_pairs:
        if cur < x:
            cur = y
            res += 1
    return res
