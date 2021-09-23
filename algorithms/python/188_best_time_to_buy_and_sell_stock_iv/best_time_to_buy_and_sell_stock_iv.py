"""
188. best time to buy and sell stock iv

https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/

买卖股票的最佳时机 IV（最多可以完成 k 笔交易）
"""
from typing import List


def max_profit(k: int, prices: List[int]) -> int:
    """
    这道题理论上和 LeetCode 123（交易次数最多为2） 的解法一样，但是直接提交容易出现超内存的错误，是 DP Table 太大导致的。
    有效的交易由买入和卖出构成，至少需要两天；反之，当天买入当天卖出则视为一次无效交易。
    题目整体思路是判断 k 和 n/2 的大小关系，两个分支分别用 LeetCode 123 和 LeetCode 122 的代码解决，可有效防止内存超出。
    """
    if not prices:
        return 0
    n = len(prices)
    if k >= n // 2:
        # 退化为不限制交易次数
        prev = prices[0]
        profit = 0
        for price in prices[1:]:
            if price > prev:
                profit += (price - prev)
            prev = price
        return profit
    else:
        # 限制交易次数为k
        max_k = k
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for j in range(1, max_k + 1):
                if i - 1 == -1:
                    # 处理 base case
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])

        return dp[n - 1][max_k][0]
