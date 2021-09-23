"""
151 reverse words in a strings

翻转字符串里的单词
"""


def reverse_words(s: str) -> str:
    """
    方法一：语言特性
    """
    return ' '.join(reversed(s.split()))
