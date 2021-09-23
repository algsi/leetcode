"""
290. word pattern

https://leetcode.com/problems/word-pattern/
https://leetcode-cn.com/problems/word-pattern/

单词规律
"""


class Solution:
    def word_pattern(self, pattern: str, s: str) -> bool:
        ch2word = {}
        word2ch = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False

        for ch, word in zip(pattern, words):
            if (word in word2ch and word2ch[word] != ch) or (ch in ch2word and ch2word[ch] != word):
                return False
            word2ch[word] = ch
            ch2word[ch] = word

        return True
