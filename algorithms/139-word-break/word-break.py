"""
139. word break

单词拆分
"""

from typing import List


def word_break_1(s: str, wordDict: List[str]) -> bool:
    """
    动态规划（未剪枝）
    :return:
    """
    if not s:
        return False
    word_set = set(wordDict)

    dp = [False for _ in range(len(s) + 1)]
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i - 1, -1, -1):
            if s[j: i] in word_set and dp[j]:
                dp[i] = True
                break

    return dp[len(s)]


def word_break_2(s: str, wordDict: List[str]) -> bool:
    """
    动态规划
    剪枝：枚举分割点的时候倒着枚举，如果分割点 j 到 i 的长度已经大于字典列表里最长的单词的长度，那么就结束枚举
    """
    pass


if __name__ == '__main__':
    param1 = 'catsandog'
    param2 = ["cats", "dog", "sand", "and", "cat"]
    res = word_break_1(param1, param2)
    print(res)
