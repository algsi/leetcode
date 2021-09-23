"""
1337. the k weakest rows in a matrix

https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/

矩阵中战斗力最弱的 K 行
"""
import heapq
from typing import List
import bisect


def k_weakest_rows(mat: List[List[int]], k: int) -> List[int]:
    """
    二分查找 + 堆
    """
    m, n = len(mat), len(mat[0])
    power = list()
    for i in range(m):
        l, r, pos = 0, n - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if mat[i][mid] == 0:
                r = mid - 1
            else:
                pos = mid
                l = mid + 1
        power.append((pos + 1, i))
    heapq.heapify(power)
    ans = list()
    for i in range(k):
        ans.append(heapq.heappop(power)[1])
    return ans
