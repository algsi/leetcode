"""
376. wiggle subsequence

https://leetcode.com/problems/wiggle-subsequence/
https://leetcode-cn.com/problems/wiggle-subsequence/

摆动序列
"""

from typing import List


class Solution:

    def wiggle_max_length(self, nums: List[int]) -> int:
        """
        动态规划

        时间复杂度：O(n)
        空间复杂度：O(n)
        """
        n = len(nums)
        if n < 2:
            return n
        up = [1] + [0] * (n - 1)
        down = [1] + [0] * (n - 1)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = max(up[i - 1], down[i - 1] + 1)
                down[i] = down[i - 1]
            elif nums[i] < nums[i - 1]:
                up[i] = up[i - 1]
                down[i] = max(down[i - 1], up[i - 1] + 1)
            else:
                up[i] = up[i - 1]
                down[i] = down[i - 1]

        return max(up[n - 1], down[n - 1])

    def wiggle_max_length_2(self, nums: List[int]) -> int:
        """
        优化的动态规划

        时间复杂度：O(n)
        空间复杂度：O(1)
        """
        n = len(nums)
        if n < 2:
            return n
        up = 1
        down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = max(up, down + 1)
                down = down
            elif nums[i] < nums[i - 1]:
                up = up
                down = max(down, up + 1)
            else:
                up = up
                down = down

        return max(up, down)

    def wiggle_max_length_3(self, nums: List[int]) -> int:
        """
        贪心
        """

        pass
