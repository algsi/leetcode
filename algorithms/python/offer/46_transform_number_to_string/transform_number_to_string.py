"""
面试题46. 把数字翻译成字符串

https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/
"""


def translate_num(num: int) -> int:
    """
    动态规划
    """
    if not num:
        return 0
    if 0 <= num <= 9:
        return 1
    s = str(num)
    dp = [0 for _ in range(len(s))]
    dp[0] = 1
    for i in range(1, len(s)):
        # 将该数字独立翻译成一个字母
        dp[i] += dp[i - 1]

        # 如果该数字能和前一个数字组合翻译成一个字母，注意 01 这种情况不能翻译成字母 b
        sub = s[i - 1] + s[i]
        if '10' <= sub <= '25':
            if i >= 2:
                dp[i] += dp[i - 2]
            else:
                dp[i] += 1

    return dp[-1]
