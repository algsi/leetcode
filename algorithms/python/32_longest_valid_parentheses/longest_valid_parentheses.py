"""
32. longest valid parentheses

最长有效括号
"""


def longest_valid_parentheses(s: str) -> int:
    """
    动态规划
    """
    if not s:
        return 0
    n = len(s)
    if n == 1:
        return 0
    dp = [0] * n
    dp[0] = 0
    dp[1] = 2 if s[0] == '(' and s[1] == ')' else 0
    res = dp[1]
    for i in range(2, n):
        if s[i] == '(':
            dp[i] = 0
        elif s[i - 1] == '(':
            dp[i] = dp[i - 2] + 2
        elif (i - dp[i - 1] - 1 >= 0) and s[i - dp[i - 1] - 1] == '(':
            dp[i] = 2 + dp[i - 1]
            if i - dp[i - 1] - 2 >= 0:
                dp[i] += dp[i - dp[i - 1] - 2]

        if dp[i] > res:
            res = dp[i]

    return res
