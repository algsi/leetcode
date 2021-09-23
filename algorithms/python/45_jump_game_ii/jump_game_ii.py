"""
45. jump game ii

https://leetcode.com/problems/jump-game-ii/
https://leetcode-cn.com/problems/jump-game-ii/

跳跃游戏 II
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0

        dp = [0] * len(nums)
        right_most = 0
        target = len(nums) - 1
        dp[0] = 0

        for i in range(len(nums)):
            tmp_right_most = max(right_most, i + nums[i])
            if tmp_right_most >= target:
                # 从当前位置可以跳到目标处
                return dp[i] + 1
            elif right_most < i + nums[i]:
                # 刷新一下标记
                self.mark(dp, i, right_most + 1, i + nums[i])

            right_most = tmp_right_most

    def mark(self, dp: List[int], cur, start, end):
        for i in range(start, end + 1):
            dp[i] = dp[cur] + 1

    def jump_2(self, nums: List[int]) -> int:
        """
        贪心算法：正向查找可到达的最大位置
        对于数组 [2,3,1,2,4,2,3]，初始位置是下标 0，从下标 0 出发，最远可到达下标 2。下标 0 可到达的位置中，下标 1 的值是 3，从下标 1 出发可以达到更远的位置，因此第一步到达下标 1。
        从下标 1 出发，最远可到达下标 4。下标 1 可到达的位置中，下标 4 的值是 4 ，从下标 4 出发可以达到更远的位置，因此第二步到达下标 4。
        因此我们的贪心策略就是要选下一步能到达的最远路径
        """
        n = len(nums)
        max_pos, end, step = 0, 0, 0
        for i in range(n - 1):
            if max_pos >= i:
                max_pos = max(max_pos, i + nums[i])
                if i == end:
                    end = max_pos
                    step += 1
        return step
