"""
378. kth smallest element in a sorted matrix

https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/

有序矩阵中第K小的元素
"""

from typing import List


def kth_smallest(matrix: List[List[int]], k: int) -> int:
    """
    binary search

    在二维结构中使用二分查找
    """
    n = len(matrix)

    def check(mid):
        i, j = n - 1, 0
        count = 0
        while i >= 0 and j < n:
            if matrix[i][j] <= mid:
                count += i + 1
                j += 1
            else:
                i -= 1

        return count >= k

    left, right = matrix[0][0], matrix[-1][-1]
    while left < right:
        mid = (right - left) // 2 + left
        if check(mid):
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8
    r = kth_smallest(matrix, k)
    print(r)
