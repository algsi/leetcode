"""
771 jewels and stones

https://leetcode-cn.com/problems/jewels-and-stones/
https://leetcode.com/problems/jewels-and-stones/
"""


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0

        j_set = {i for i in J}

        ans = 0
        for s in S:
            if s in j_set:
                ans += 1
        return ans
