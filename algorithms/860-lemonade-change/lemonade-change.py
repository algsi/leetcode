"""
860. lemonade change

https://leetcode.com/problems/lemonade-change/
https://leetcode-cn.com/problems/lemonade-change/

柠檬水找零
"""

from typing import List


class Solution:
    """
    模拟 + 贪心
    """
    def lemonade_change(self, bills: List[int]) -> bool:
        change_five, change_ten = 0, 0
        for bill in bills:
            if bill == 5:
                change_five += 1
            elif bill == 10:
                # 找零 5 元
                if change_five == 0:
                    return False
                else:
                    change_five -= 1
                    change_ten += 1
            else:
                # 找零 15 元，优先把零钱 10 元用出去
                if change_ten > 0 and change_five >= 1:
                    change_ten -= 1
                    change_five -= 1
                elif change_five >= 3:
                    change_five -= 3
                else:
                    return False
        return True
