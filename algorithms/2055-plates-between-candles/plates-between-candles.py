"""
2055 plates between candles

蜡烛之间的盘子
"""
from typing import List

def plates_between_candles(s: str, queries: List[List[int]]) -> List[int]:
    """
    前缀和 + 预处理
    """
    n = len(s)
    pre_sum = [0] * n
    left = [0] * n
    right = [0] * n

    tmp_pre_sum, l = 0, -1
    for i, ch in enumerate(s):
        if ch == '*':
            tmp_pre_sum += 1
        else:
            l = i
        pre_sum[i] = tmp_pre_sum
        left[i] = l
    
    r = n - 1
    for i in range(n - 1, -1, - 1):
        if s[i] == '|':
            r = i
        right[i] = r

    ans = [0] * len(queries)
    for i, q in enumerate(queries):
        x, y = right[q[0]], left[q[1]]
        if x >= 0 and y >= 0 and x < y:
            ans[i] = pre_sum[y] - pre_sum[x]
    return ans
