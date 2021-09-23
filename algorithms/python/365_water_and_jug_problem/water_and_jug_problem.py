"""
365. water and jug problem

https://leetcode.com/problems/water-and-jug-problem/
https://leetcode-cn.com/problems/water-and-jug-problem/

水壶问题
"""


class Solution:
    """
    深度优先搜索

    complexity analysis
    time complexity: O(xy)，状态数量最多有 (x+1)(y+1) 种，对每一种状态进行深度优先搜索的时间复杂度为 O(1)，因此总时间复杂度为 O(xy)
    space complexity: O(xy)，由于状态数量最多有 (x+1)(y+1) 种，哈希集合中最多会有 (x+1)(y+1) 项，因此空间复杂度为 O(xy)O(xy)。
    """

    def can_measure_water(self, x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()

        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            # python 中比较元组会逐个比较其中的元素
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False
