"""
518. coin change 2

https://leetcode.com/problems/coin-change-2/
https://leetcode-cn.com/problems/coin-change-2/

零钱兑换 II
"""
from typing import List


def change(amount: int, coins: List[int]) -> int:
    """
    背包 DP
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]


if __name__ == '__main__':
    change(1, [])
