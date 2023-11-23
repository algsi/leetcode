"""
1018. binary prefix divisible by 5

https://leetcode.com/problems/binary-prefix-divisible-by-5/
https://leetcode-cn.com/problems/binary-prefix-divisible-by-5/

可被 5 整除的二进制前缀
"""

from typing import List


class Solution:
    def prefixes_div_by_5(self, A: List[int]) -> List[bool]:
        ans = list()
        prefix = 0
        for num in A:
            prefix = ((prefix << 1) + num) % 5
            ans.append(prefix == 0)
        return ans
