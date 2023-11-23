"""
345. reverse vowels of a string

https://leetcode.com/problems/reverse-vowels-of-a-string/
https://leetcode-cn.com/problems/reverse-vowels-of-a-string/

反转字符串中的元音字母
"""


def reverse_vowels(s: str) -> str:
    sets = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    t = list(s)
    n = len(s)
    i, j = 0, n - 1
    while i < j:
        while i < n and s[i] not in sets:
            i += 1
        while j > 0 and s[j] not in sets:
            j -= 1
        if i < j:
            t[i], t[j] = t[j], t[i]
            i += 1
            j -= 1
    return ''.join(t)
