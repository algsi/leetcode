"""
413 arithmetic slices

https://leetcode.com/problems/arithmetic-slices/
https://leetcode-cn.com/problems/arithmetic-slices/

等差数列划分
"""


def number_of_arithmetic_slices(nums: List[int]) -> int:
    n = len(nums)
    if n == 1:
        return 0
    d, t = nums[0] - nums[1], 0
    ans = 0

    # 因为等差数列的长度至少为 3，所以可以从 i=2 开始枚举
    for i in range(2, n):
        if nums[i - 1] - nums[i] == d:
            t += 1
        else:
            d = nums[i - 1] - nums[i]
            t = 0
        ans += t
    return ans
