"""
122. best time to buy and sell stock ii

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/

买卖股票的最佳时机 II（不限制交易次数）
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    """
    贪心算法

    简单的一次遍历，只要前后两次有利益可得就做一次买卖，因为次数不受限制
    """
    profit = 0
    n = len(prices)
    for i in range(1, n):
        profit += max(0, prices[i] - prices[i - 1])
    return profit
