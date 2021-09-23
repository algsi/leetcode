"""
576. out of boundary paths

https://leetcode.com/problems/out-of-boundary-paths/
https://leetcode-cn.com/problems/out-of-boundary-paths/

出界的路径数
"""


def find_paths(m: int, n: int, max_move: int, start_row: int, start_column: int) -> int:
    mod = 10 ** 9 + 7
    out_counts = 0
    dp = [[0] * n for _ in range(m)]
    dp[start_row][start_column] = 1
    for i in range(max_move):
        dp_new = [[0] * n for _ in range(m)]
        for j in range(m):
            for k in range(n):
                if dp[j][k] > 0:
                    for j1, k1 in [(j - 1, k), (j + 1, k), (j, k - 1), (j, k + 1)]:
                        if 0 <= j1 < m and 0 <= k1 < n:
                            dp_new[j1][k1] = (dp_new[j1][k1] + dp[j][k]) % mod
                        else:
                            out_counts = (out_counts + dp[j][k]) % mod
        dp = dp_new
    return out_counts
