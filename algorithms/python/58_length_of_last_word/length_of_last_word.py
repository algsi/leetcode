"""
58. length of last word

最后一个单词的长度
"""


def length_of_last_word(s: str) -> int:
    if not s:
        return 0
    ret = 0
    for i in range(len(s) - 1, -1, -1):
        if ' ' == s[i]:
            if ret != 0:
                return ret
            else:
                continue

        ret += 1

    return ret
