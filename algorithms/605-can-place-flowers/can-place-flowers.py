"""
605. can place flowers

https://leetcode.com/problems/can-place-flowers/
https://leetcode-cn.com/problems/can-place-flowers/

种花问题
"""

from typing import List


class Solution:
    """
    贪心
    """

    def can_place_flowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        count = 0  # 可以种入花的数量
        prev = -2  # 表示上一朵已经种植的花的下标位
        for i in range(length):
            if flowerbed[i] == 1:
                prev = i
            else:
                if i - prev > 1:
                    if i < length - 1 and flowerbed[i + 1] == 1:
                        continue
                    # can place
                    count += 1
                    if count == n:
                        return True
                    prev = i
        return count >= n
