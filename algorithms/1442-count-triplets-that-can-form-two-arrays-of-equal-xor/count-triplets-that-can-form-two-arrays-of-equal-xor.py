"""
1442. count triplets that can form two arrays of equal xor

https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/
https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

形成两个异或相等数组的三元组数目
"""

from typing import List
import collections


def count_triplets(arr: List[int]) -> int:
    """
    哈希表：一重循环
    """
    n = len(arr)
    s = collections.defaultdict(lambda: 0)
    for i, val in enumerate(arr):
        s[i + 1] = s[i] ^ val
    ans = 0
    cnt = collections.defaultdict(lambda: 0)
    total = collections.defaultdict(lambda: 0)
    for k in range(0, n):
        m = cnt.get(s[k + 1], None)
        if m:
            ans += m * k - total[s[k + 1]]
        cnt[s[k]] += 1
        total[s[k]] += k
    return ans
