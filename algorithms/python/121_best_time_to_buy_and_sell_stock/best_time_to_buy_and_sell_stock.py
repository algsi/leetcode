"""
121. best time to buy and sell stock

买卖股票的最佳时机（只能买卖一次）
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    一次遍历

    记录历史最低价格和当前最大利润
    """
    if prices is None or len(prices) < 2:
        return 0
    prev_min = prices[0]
    profit = 0
    for price in prices[1:]:
        if price > prev_min:
            profit = max(price - prev_min, profit)
        else:
            prev_min = price

    return profit
