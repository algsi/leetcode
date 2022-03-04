"""
452. minimum number of arrows to burst balloons

https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons/

用最少数量的箭引爆气球
"""

from typing import List


class Solution:
    """
    排序 + 贪心算法

    complexity analysis
    time complexity: O(nlogn)，此为排序时间复杂度
    space complexity：O(logn)，排序所需要的栈空间
    """

    def find_min_arrow_shots(self, points: List[List[int]]) -> int:
        # sort by end position
        points.sort(key=lambda x: x[1])
        pos = points[0][1]  # 上一次射到的边界，这个边界一定是一个气球的 end point
        output = 1
        for start, end in points:
            if start > pos:
                pos = end
                output += 1
        return output
