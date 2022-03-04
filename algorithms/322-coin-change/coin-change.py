"""
322. coin change

零钱兑换
"""

from typing import List
import sys


class Solution:
    def coin_change(self, coins: List[int], amount: int) -> int:
        return self.__coin_change(0, coins, amount)

    def __coin_change(self, idx_coin: int, coins: List[int], amount: int) -> int:
        """
        搜索回溯

        时间复杂度：O(S^n)
        空间复杂度：O(n)
        """
        if amount == 0:
            return 0
        if idx_coin < len(coins) and amount > 0:
            max_val = amount // coins[idx_coin]  # 当前面值硬币最多可以取多少个
            min_cost = sys.maxsize

            # 尝试使用不同个数当前面值硬币
            for i in range(max_val + 1):
                if amount >= i * coins[idx_coin]:
                    # recursive
                    res = self.__coin_change(idx_coin + 1, coins, amount - i * coins[idx_coin])
                    if res != -1:
                        min_cost = min(min_cost, res + i)

            return -1 if min_cost == sys.maxsize else min_cost

        # 没有任何一种组合满足条件
        return -1

    def coin_change_2(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        return self.__coin_change_2(coins, amount, [0] * amount)

    def __coin_change_2(self, coins: List[int], amount: int, count: List[int]) -> int:
        """
        自顶向下的动态规划：F(S) = F(S - C) + 1

        :param coins:  硬币面值列表
        :param amount: 需要满足的金额
        :param count:  记录，避免重复计算
        """

        if count[amount - 1] != 0:
            return count[amount - 1]

        min_cost = sys.maxsize
        for coin in coins:
            if coin == amount:
                min_cost = 1
                break
            elif coin > amount:
                continue
            else:
                res = self.__coin_change_2(coins, amount - coin, count)
                if res != -1 and res < min_cost:
                    min_cost = res + 1

        count[amount - 1] = -1 if min_cost == sys.maxsize else min_cost
        return count[amount - 1]


