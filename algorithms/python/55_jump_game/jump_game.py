"""
55. jump game

跳跃游戏
"""

from typing import List


def can_jump(nums: List[int]) -> bool:
    """
    贪心算法
    在遍历的过程中，如果最远可以到达的位置大于等于数组中的最后一个位置，那就说明最后一个位置可达，我们就可以直接返回 True 作为答案。
    反之，如果在遍历结束后，最后一个位置仍然不可达，我们就返回 False 作为答案。

    complexity analysis
    time complexity: O(n)
    space complexity: O(1)
    """

    right_most = 0  # 能跳到最远的位置
    target = len(nums) - 1  # 目标位置
    for i in range(len(nums)):
        if right_most >= target:
            # 可以跳到目标处
            return True

        if right_most >= i:
            # 可以跳到当前位置来，更新可以跳到到最远位置
            right_most = max(right_most, i + nums[i])
        else:
            return False

    return False


def can_jump_2(nums: List[int]) -> bool:
    """
    动态规划
    dp[i] 表示从 0 走到 i 后下一个能到达的最远的下标，那么 dp[i] = max(dp[i - 1], i + nums[i])
    如果不可达，则返回 False
    可以看到，在这个动态规划中我们实际上只需要保留上一个能到达的最远的位置即可，所以可以不用数组来存储所有的记录
    """
    pass
