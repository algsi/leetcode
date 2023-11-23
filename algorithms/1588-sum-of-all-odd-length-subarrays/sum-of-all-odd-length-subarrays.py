"""
1588. sum of all odd length subarrays

https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays/

所有奇数长度子数组的和
"""


def sum_odd_length_subarrays(arr: List[int]) -> int:
    """
    前缀和 prefix_sum 表示数组从下标 0 到下标 i-1 的元素和
    """
    n = len(arr)
    prefix_sum = [0] * (n + 1)
    for i in range(0, n):
        prefix_sum[i + 1] = prefix_sum[i] + arr[i]
    ret = 0
    for start in range(0, n):
        for length in range(1, n - start + 1, 2):
            end = start + length - 1
            ret += prefix_sum[end + 1] - prefix_sum[start]
    return ret
