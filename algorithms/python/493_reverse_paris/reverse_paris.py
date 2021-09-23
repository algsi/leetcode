"""
493. reverse pairs

https://leetcode.com/problems/reverse-pairs/
https://leetcode-cn.com/problems/reverse-pairs/

翻转对
"""

from typing import List


class Solution:
    def reverse_pairs(self, nums: List[int]) -> int:
        if not nums:
            return 0

        def reverse_pairs_recursive(left: int, right: int) -> int:
            if left == right:
                return 0
            mid = (right - left) // 2 + left
            ret = reverse_pairs_recursive(left, mid) + reverse_pairs_recursive(mid + 1, right)
            # 首先统计下标对的数量
            i = left
            j = mid + 1
            while i <= mid:
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                ret += j - mid - 1
                i += 1

            # 随后合并两个排序数组
            p1 = left
            p2 = mid + 1
            p = left
            while p1 <= mid or p2 <= right:
                if p1 > mid:
                    aux[p] = nums[p2]
                    p2 += 1
                elif p2 > right:
                    aux[p] = nums[p1]
                    p1 += 1
                else:
                    if nums[p1] < nums[p2]:
                        aux[p] = nums[p1]
                        p1 += 1
                    else:
                        aux[p] = nums[p2]
                        p2 += 1
                p += 1

            for k in range(left, right + 1):
                nums[k] = aux[k]
            return ret

        n = len(nums)
        aux = [0] * n
        return reverse_pairs_recursive(0, n - 1)
