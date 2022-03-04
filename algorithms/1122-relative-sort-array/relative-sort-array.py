"""
1122. relative sort array

https://leetcode.com/problems/relative-sort-array/
https://leetcode-cn.com/problems/relative-sort-array/

数组的相对排序
"""

from typing import List


class Solution:
    def relative_sort_array(self, arr1: List[int], arr2: List[int]) -> List[int]:
        rank = {arr2[i]: i for i in range(len(arr2))}

        def comparator(x: int) -> (int, int):
            """
            self defined comparator

            返回元组，python 可以基于元组比较，即依次比较元组中每一个对应位置的元素，直到比较出大小关系为止。
            """

            if x in rank:
                return 0, rank[x]
            else:
                return 1, x

        arr1.sort(key=comparator)
        return arr1
