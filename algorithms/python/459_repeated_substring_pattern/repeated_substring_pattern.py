"""
459. repeated substring pattern

重复的子字符串
"""


def repeated_substring_pattern(s: str) -> bool:
    end = 0
    offset = 0
    i = 1
    n = len(s)
    res = False
    while i < n:
        if s[i] != s[offset]:
            offset = 0
            end += 1
            i = end + 1
        else:
            i += 1
            offset += 1

        if offset > end:
            offset = 0
            res = True
        else:
            res = False

    return res


def main():
    s = 'abcdababcdab'
    print(repeated_substring_pattern(s))


if __name__ == '__main__':
    main()
