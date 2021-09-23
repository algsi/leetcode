"""
557. reverse words in a string iii

反转字符串中的单词 III
"""


def reverse_words(s: str) -> str:
    if not s:
        return s

    res = ''
    tmp = ''
    for i in s:
        if i == ' ':
            res = res + tmp + ' '
            tmp = ''
        else:
            tmp = i + tmp

    return res + tmp


def main():
    param = "Let's take LeetCode contest"
    print(reverse_words(param))


if __name__ == '__main__':
    main()
