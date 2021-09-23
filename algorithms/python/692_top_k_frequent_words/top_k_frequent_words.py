"""
692. top k frequent words

https://leetcode.com/problems/top-k-frequent-words/
https://leetcode-cn.com/problems/top-k-frequent-words/

前K个高频单词
"""

import collections
from functools import cmp_to_key
from typing import List


def topKFrequent(words: List[str], k: int) -> List[str]:
    """
    哈希表 + 排序
    """
    counter = collections.Counter(words)

    def cmp(a: str, b: str):
        if counter[a] > counter[b] or (counter[a] == counter[b] and a < b):
            return -1
        return 1

    return sorted(counter.keys(), key=cmp_to_key(cmp))[:k]
