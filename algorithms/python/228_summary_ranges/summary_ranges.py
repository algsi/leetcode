"""
228. summary ranges

https://leetcode.com/problems/summary-ranges/
https://leetcode-cn.com/problems/summary-ranges/

汇总区间
"""

from typing import List


class Solution:
    """
    一次遍历
    """

    def summary_ranges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n = len(nums)
        prev_idx, cur_idx = 0, 0
        output = []
        for i in range(1, n):
            if nums[i] == nums[cur_idx] + 1:
                cur_idx = i
            else:
                output.append(self.get_str(nums[prev_idx], nums[cur_idx]))
                prev_idx = cur_idx = i
        output.append(self.get_str(nums[prev_idx], nums[cur_idx]))
        return output

    @staticmethod
    def get_str(start: int, end: int) -> str:
        if start == end:
            return str(start)
        return str(start) + '->' + str(end)
