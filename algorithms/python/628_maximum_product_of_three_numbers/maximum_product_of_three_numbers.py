"""
628. maximum product of three numbers

https://leetcode.com/problems/maximum-product-of-three-numbers/
https://leetcode-cn.com/problems/maximum-product-of-three-numbers/

三个数的最大乘积
"""

from typing import List


class Solution:
    def maximum_product(self, nums: List[int]) -> int:
        # 最小的和第二小的
        min1, min2 = float('inf'), float('inf')
        # 最大的、第二大的和第三大的
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')
        for num in nums:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num

            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
        return max(max1 * max2 * max3, max1 * min1 * min2)
