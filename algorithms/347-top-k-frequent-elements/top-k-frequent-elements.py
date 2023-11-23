"""
347. top k frequent elements

https://leetcode-cn.com/problems/top-k-frequent-elements/

347. 前 K 个高频元素
"""

import collections
import heapq


def top_k_frequent_1(nums, k):
    """
    哈希表 + 堆

    手写实现堆
    """
    count = collections.Counter(nums)

    pass


def top_k_frequent_2(nums, k):
    """
    借助 collections.Counter#most_common
    """
    count = collections.Counter(nums)
    return heapq.nlargest(k, count.keys(), key=count.get)


def top_k_frequent_3(nums, k):
    """
    借助 collections.Counter#most_common
    """
    counter = collections.Counter(nums)
    return [key for key, freq in counter.most_common(k)]

