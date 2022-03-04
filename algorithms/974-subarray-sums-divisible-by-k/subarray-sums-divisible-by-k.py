"""
974. subarray sums divisible by k

https://leetcode.com/problems/subarray-sums-divisible-by-k/
https://leetcode-cn.com/problems/subarray-sums-divisible-by-k/

和可被 K 整除的子数组
"""
from typing import List


def subarray_div_by_k(A: List[int], K: int) -> int:
    """
    前缀和 + 哈希表 + 同余定理

    See: LeetCode 560 subarray sum equals k
    """
    ans = 0
    total = 0
    # 考虑前缀和本身被 K 整除的情况
    record = {0: 1}
    for num in A:
        total += num
        module = total % K
        same = record.get(module, 0)
        ans += same
        record[module] = same + 1
    return ans
