"""
242. valid anagram

https://leetcode.com/problems/valid-anagram/
https://leetcode-cn.com/problems/valid-anagram/

有效的字母异位词
"""

import collections


class Solution:

    def is_anagram(self, s: str, t: str) -> bool:
        """
        sort
        """
        if len(s) != len(t):
            return False
        list1 = list(s)
        list2 = list(t)
        list1.sort()
        list2.sort()
        return list1 == list2

    def is_anagram2(self, s: str, t: str) -> bool:
        """
        hash table
        """
        return collections.Counter(s) == collections.Counter(t)


def main():
    s = 'a'
    t = 'b'
    solution = Solution()
    print(solution.is_anagram(s, t))


if __name__ == '__main__':
    main()
