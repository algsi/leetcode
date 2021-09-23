"""
217. contains duplicate

https://leetcode.com/problems/contains-duplicate/
https://leetcode-cn.com/problems/contains-duplicate/

存在重复元素
"""
from typing import List


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
