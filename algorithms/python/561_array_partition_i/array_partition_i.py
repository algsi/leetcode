"""
561. array partition

https://leetcode-cn.com/problems/array-partition-i/

数组拆分 I
"""

from typing import List


def array_pair_sum(nums: List[int]) -> int:
    """
    简单的一道题，关键是证明

    用递归的思想就比较好理解

    首先找到最小值 x ，它跟任何其他值配对，min([x, anything]) 都会得到 x。而 anything 取次小值时对剩下的数损耗最小，所以跟 x 配对的是次小值。
    余下的数同理，所以最佳方案是先将数组排序，再两两配对。
    """
    return sum(sorted(nums)[::2])
