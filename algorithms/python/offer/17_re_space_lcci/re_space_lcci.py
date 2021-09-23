"""
面试题 17.13. 恢复空格

https://leetcode-cn.com/problems/re-space-lcci/
"""

from typing import List


def respace(dictionary: List[str], sentence: str) -> int:
    """
    DP

    该题和 139（单词拆分）做法相同
    """
    if not sentence:
        return 0
    words = set()
    max_length = 0  # 用于剪枝
    for d in dictionary:
        words.add(d)
        max_length = max(max_length, len(d))
    dp = [0]
    for i in range(len(sentence)):
        dp.append(dp[i] + 1)
        # 尝试让未识别的字符最少
        for j in range(i, -1, -1):
            if i - j + 1 > max_length:
                # 剪枝
                break
            if sentence[j: i + 1] in words:
                dp[i + 1] = min(dp[i + 1], dp[j])

    return dp[len(sentence)]


if __name__ == '__main__':
    dictionary = ["sssjjs", "hschjf", "hhh", "fhjchfcfshhfjhs", "sfh", "jsf", "cjschjfscscscsfjcjfcfcfh",
                  "hccccjjfchcffjjshccsjscsc", "chcfjcsshjj", "jh", "h", "f", "s", "jcshs", "jfjssjhsscfc"]
    sentence = "sssjjssfshscfjjshsjjsjchffffs"
    r = respace(dictionary, sentence)
    print(r)
