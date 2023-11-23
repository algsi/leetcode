"""
22. generate parentheses

括号生成
"""

from typing import List


class Solution:
    """
    暴力法
    """
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.generate([], n, ans)
        return ans

    def generate(self, cache: List[str], n: int, ans: List[str]):
        if len(cache) == 2 * n:
            if self.valid(cache):
                ans.append("".join(cache))
            return

        cache.append('(')
        self.generate(cache, n, ans)
        cache.pop()
        cache.append(')')
        self.generate(cache, n, ans)
        cache.pop()

    def valid(self, cache: List[str]):
        bal = 0
        for c in cache:
            if c == '(':
                bal += 1
            else:
                bal -= 1
            if bal < 0:
                return False
        return bal == 0
