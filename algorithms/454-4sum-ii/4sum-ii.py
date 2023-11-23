"""
454. 4sum ii

https://leetcode.com/problems/4sum-ii/
https://leetcode-cn.com/problems/4sum-ii/

四数相加 II
"""

from typing import List


class Solution:
    """
    分组 + 哈希表

    我们可以将四个数组分成两部分，A 和 B 为一组，C 和 D 为另外一组。
    对于 A 和 B，我们使用二重循环对他们进行遍历，得到所有的 A[i] + B[j] 的值并存入哈希表中。对于哈希映射中的每个键值对，每个键
    表示一种 A[i] + B[j]，对应的值为 A[i] + B[j] 出现的次数。

    对于 C 和 D，我们同样使用二重循环对它们进行遍历。当遍历到 C[k] + D[l] 时，如果 -(C[k] + D[l]) 出现在哈希映射中，
    那么将 -(C[k] + D[l]) 对应的值累加进答案中。

    complexity analysis
    time complexity: O(n^2)
    space complexity: O(n^2)
    """

    def four_sum_count(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dict1 = self.to_dict(A, B)
        output = 0
        for i in C:
            for j in D:
                s = i + j
                count = dict1[-s]
                if count is not None:
                    output += count

        return output

    @staticmethod
    def to_dict(list1: List[int], list2: List[int]):
        res = dict()
        for i in list1:
            for j in list2:
                s = i + j
                count = res.get(s, 0) + 1
                res[s] = count
        return res
