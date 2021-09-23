"""
973. k closest points to origin

https://leetcode.com/problems/k-closest-points-to-origin/
https://leetcode-cn.com/problems/k-closest-points-to-origin/

最接近原点的 K 个点
"""

from typing import List
import heapq
import random


class Solution:
    """
    用欧几里得距离的平方，避免数据误差
    """

    def k_closest_1(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        sort

        complexity analysis
        time complexity: O(nlogn)
        space complexity: O(nlogn)
        """
        points.sort(key=lambda x: (x[0] ** 2 + x[1] ** 2))
        return points[:K]

    def k_closest_2(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        priority queue

        我们可以使用一个优先队列（大顶堆）实时维护前 K 个最小的距离平方。

        complexity analysis:
        time complexity: O(nlogK)。其中 n 是数组 points 的长度，由于优先队列维护的是前 K 个距离最小的节点，因此弹出和插入操作的单次时间复杂度均是 O(logK)，
        在最坏情况下，数组里 n 个节点都会插入，因此时间复杂度为 O(nlogK)。
        space complexity: O(K)。因为优先队列中最多有 K 个节点
        """
        pq = [(- x ** 2 - y ** 2, i) for i, (x, y) in enumerate(points[:K])]
        heapq.heapify(pq)
        n = len(points)
        for i in range(K, n):
            x, y = points[i]
            dist = -x ** 2 - y ** 2
            heapq.heappushpop(pq, (dist, i))
        ans = [points[i] for (_, i) in pq]
        return ans

    def k_closest_3(self, points: List[List[int]], K: int) -> List[List[int]]:
        """
        quick sort

        时间复杂度：期望为 O(n)
        空间复杂度：期望为 O(logn)，即为递归调用深度
        """

        def random_select(left: int, right: int, k: int):
            """
            :param left the left border index (inclusive)
            :param right the right border index (inclusive)
            :param k the number of element
            """
            if right - left + 1 <= k:
                return
            # select the random element as a base element
            pivot_id = random.randint(left, right)
            pivot = points[pivot_id][0] ** 2 + points[pivot_id][1] ** 2
            points[right], points[pivot_id] = points[pivot_id], points[right]

            # dual pointer
            i = left - 1
            for j in range(left, right):
                if points[j][0] ** 2 + points[j][1] ** 2 <= pivot:
                    i += 1
                    points[i], points[j] = points[j], points[i]
            i += 1
            points[i], points[right] = points[right], points[i]
            # [left, i - 1] 都小于等于 pivot，[i + 1, right] 都大于 pivot，[i] 等于 pivot
            if k < i - left + 1:
                random_select(left, i - 1, k)
            elif k > i - left + 1:
                random_select(i + 1, right, k - (i - left + 1))

        n = len(points)
        random_select(0, n - 1, K)
        return points[:K]
