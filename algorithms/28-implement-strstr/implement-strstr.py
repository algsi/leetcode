"""
28. implement strstr

https://leetcode-cn.com/problems/implement-strstr/comments/

实现 strStr()
"""


def str_str(haystack: str, needle: str) -> int:
    return haystack.find(needle)


if __name__ == '__main__':
    print(str_str("hello", "ll"))
