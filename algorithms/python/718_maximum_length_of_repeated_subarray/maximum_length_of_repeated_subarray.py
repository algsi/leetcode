"""
718. maximum length of repeated subarray

最长重复子数组
"""

from typing import List


def find_length(A: List[int], B: List[int]) -> int:
    """
    dynamic programming

    时间复杂度：O(N×M)
    空间复杂度：O(N×M)
    """
    if not A or not B:
        return 0
    ans = 0
    n, m = len(A), len(B)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(0, n):
        for j in range(0, m):
            dp[i + 1][j + 1] = dp[i][j] + 1 if A[i] == B[j] else 0
            ans = max(ans, dp[i + 1][j + 1])

    return ans


if __name__ == '__main__':
    arr1 = [0, 0, 0, 0, 0]
    arr2 = [0, 0, 0, 0, 0]
    print(find_length(arr1, arr2))
