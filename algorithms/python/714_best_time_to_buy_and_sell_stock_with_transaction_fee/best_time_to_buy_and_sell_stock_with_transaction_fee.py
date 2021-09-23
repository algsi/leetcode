"""
714. best time to buy and sell stock with transaction fee

买卖股票的最佳时机含手续费（不限交易次数）
"""

from typing import List


def max_profit(prices: List[int], fee: int) -> int:
    if not prices:
        return 0

    n = len(prices)
    dp_i_0, dp_i_1 = 0, float('-inf')
    for i in range(n):
        temp = dp_i_0
        dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
        dp_i_1 = max(dp_i_1, temp - prices[i] - fee)

    return dp_i_0
