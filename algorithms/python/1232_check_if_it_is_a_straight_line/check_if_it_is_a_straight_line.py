"""
1232. check if it is a straight line

https://leetcode.com/problems/check-if-it-is-a-straight-line/
https://leetcode-cn.com/problems/check-if-it-is-a-straight-line/

缀点成线
"""

from typing import List


class Solution:

    def check_straight_line(self, coordinates: List[List[int]]) -> bool:
        delta_x = coordinates[0][0]
        delta_y = coordinates[0][1]

        for coordinate in coordinates:
            coordinate[0] -= delta_x
            coordinate[1] -= delta_y

        a, b = coordinates[1][1], -coordinates[1][0]
        for coordinate in coordinates:
            x = coordinate[0], y = coordinate[1]
            if a * x + b * y != 0:
                return False
        return True
