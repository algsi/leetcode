"""
169. majority element

https://leetcode-cn.com/problems/majority-element/
https://leetcode.com/problems/majority-element/

多数元素
"""

import random
import collections
from typing import List


def majority_element_1(nums: List[int]) -> int:
    """
    Hash
    """
    counter = collections.Counter(nums)
    return max(counter.keys(), key=counter.get)


def majority_element_2(nums: List[int]) -> int:
    """
    Sort
    如果将数组 nums 中的所有元素按照单调递增或单调递减的顺序排序，那么下标为 n//2 的元素（下标从 0 开始）一定是众数。
    """
    nums.sort()
    return nums[len(nums) // 2]


def majority_element_3(nums: List[int]) -> int:
    """
    随机化

    因为超过 n//2 的数组下标被众数占据了，这样我们随机挑选一个下标对应的元素并验证，有很大的概率能找到众数。

    由于一个给定的下标对应的数字很有可能是众数，我们随机挑选一个下标，检查它是否是众数，如果是就返回，否则继续随机挑选。

    最坏时间复杂度是没有上限的
    """
    majority_count = len(nums) // 2
    while True:
        candidate = random.choice(nums)
        if sum(1 for ele in nums if ele == candidate) > majority_count:
            return candidate


def majority_element_4(nums: List[int]) -> int:
    """
    Boyer-Moore 投票算法

    https://leetcode-cn.com/problems/majority-element/solution/duo-shu-yuan-su-by-leetcode-solution/
    """
    count = 0
    candidate = 0
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate
