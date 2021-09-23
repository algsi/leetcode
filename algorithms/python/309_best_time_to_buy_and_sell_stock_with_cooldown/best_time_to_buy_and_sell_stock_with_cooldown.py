"""
309. best time to buy and sell stock with cooldown

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

最佳买卖股票时机含冷冻期
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    if not prices:
        return 0
    n = len(prices)
    dp_i_0, dp_i_1 = 0, float('-inf')
    dp_pre_0 = 0  # represent dp[i - 2][0]
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, dp_pre_0 - prices[i])
        dp_pre_0 = temp

    return dp_i_0
