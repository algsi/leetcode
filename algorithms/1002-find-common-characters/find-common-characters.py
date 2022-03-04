"""
1002. find common characters

https://leetcode.com/problems/find-common-characters/
https://leetcode-cn.com/problems/find-common-characters/
"""

from typing import List


class Solution:
    """
    暴力法
    """

    def commonChars(self, A: List[str]) -> List[str]:
        min_freq = [float('inf')] * 26
        for word in A:
            freq = [0] * 26
            for ch in word:
                freq[ord(ch) - ord('a')] += 1

            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])

        output = []
        for i in range(26):
            output.extend([chr(i + ord('a'))] * int(min_freq[i]))
        return output
