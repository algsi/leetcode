"""
1128. number of equivalent domino pairs

https://leetcode.com/problems/number-of-equivalent-domino-pairs/
https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/

等价多米诺骨牌对的数量
"""

from typing import List

"""
等价的定义是，在允许翻转两个二元对的情况下，使它们的元素一一对应相等。

于是我们不妨直接让每一个二元对都变成指定的格式，即第一堆必须不大于第二堆。这样两个二元对等价当且仅当两个二元对完全相同。

注意到二元对中的元素均不大于 9，因此我们可以直接将每个二元对拼接成一个二位的正整数，即 (x, y) -> 10 * x + y。
这样就不需要使用哈希表来统计元素数量，而直接使用数组即可。
"""


def num_equiv_domino_pairs(dominoes: List[List[int]]) -> int:
    ret = 0

    num = [0] * 100
    for x, y in dominoes:
        value = (10 * x + y if x <= y else 10 * y + x)
        ret += num[value]
        num[value] += 1
    return ret
