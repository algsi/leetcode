"""
560. subarray sum equals k

https://leetcode-cn.com/problems/subarray-sum-equals-k/
https://leetcode.com/problems/subarray-sum-equals-k/

和为K的子数组
"""

from typing import List


def subarray_sum_1(nums: List[int], k: int) -> int:
    """
    枚举
    考虑以 i 开头和为 k 的连续子数组个数，对于某个 i，我们需要确定符合条件的 j 的个数，其中 0<=i<=j 这个子数组的和恰好为K。

    时间复杂度：平方级
    空间复杂度：常数级
    """

    ans = 0

    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            # 优化求和，减少重复的计算量
            sum += nums[j]
            if sum == k:
                ans += 1

    return ans


def subarray_sum_2(nums: List[int], k: int) -> int:
    """
    前缀和 + 哈希表优化
    """
    # 初始化是为了应对 nums=[1, 1, 1], k=2 的情况，也就是首pre恰好等于k
    dic = {0: 1}
    pre, count = 0, 0
    for i in range(len(nums)):
        pre += nums[i]
        if pre - k in dic:
            count += dic[pre - k]

        dic[pre] = dic.get(pre, 0) + 1

    return count
