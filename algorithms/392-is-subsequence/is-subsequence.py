"""
392. is subsequence

判断子序列
"""


def is_subsequence(s: str, t: str) -> bool:
    """
    dynamic programming

    时间复杂度：O(len(t))
    空间复杂度：O(len(t))
    """
    if not s:
        return True

    len_s, len_t = len(s), len(t)
    if len_s > len_t:
        return False

    dp = [-1] * len_t

    if s[0] == t[0]:
        dp[0] = 0
    for i in range(1, len_t):
        dp[i] = dp[i - 1]
        if dp[i] == len_s - 1:
            return True
        if s[dp[i] + 1] == t[i]:
            dp[i] += 1
    return dp[-1] == len_s - 1


def is_subsequence_2(s: str, t: str) -> bool:
    """
    dual pointer
    """
    pass
    n, m = len(s), len(t)
    i = j = 0
    while i < n and j < m:
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == n


if __name__ == '__main__':
    pass
