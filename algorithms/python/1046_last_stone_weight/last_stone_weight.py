"""
1046. last stone weight

https://leetcode.com/problems/last-stone-weight/
https://leetcode-cn.com/problems/last-stone-weight/

最后一块石头的重量
"""

from typing import List
import heapq


class Solution:
    """
    python 只支持小顶堆，所以在入堆的时候我们要添加的是数据的相反数
    """

    def last_stone_weight(self, stones: List[int]) -> int:
        # initialize
        heap = [-stone for stone in stones]
        heapq.heapify(stones)

        # 模拟
        while len(heap) > 1:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, x - y)
        if heap:
            return - heap[0]
        return 0


class Heap:
    """
    自定义实现的堆
    """

    def __init__(self, desc=False):
        """
        初始化，默认创建一个小顶堆
        """
        self.heap = []
        self.desc = desc
