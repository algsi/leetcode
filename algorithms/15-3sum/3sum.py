"""
15. 3sum

三数之和
"""

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    """
    排序 + 双指针
    """
    nums.sort()
    if not nums or len(nums) < 3:
        return []

    ans = []
    i, n = 0, len(nums)
    while i < n - 2:
        lo = i + 1
        hi = n - 1
        while lo < hi:
            # 去重
            while n - 1 > hi > lo and nums[hi] == nums[hi + 1]:
                hi -= 1
            while hi > lo > i + 1 and nums[lo] == nums[lo - 1]:
                lo += 1

            sum_tmp = nums[i] + nums[lo] + nums[hi]
            if sum_tmp == 0:
                ans.append([nums[i], nums[lo], nums[hi]])
                hi -= 1
                lo += 1
            elif sum_tmp > 0:
                # hi decreasing
                hi -= 1
            else:
                # lo increasing
                lo += 1

        i += 1
        while i < n - 2 and nums[i] == nums[i - 1]:
            i += 1

    return ans


if __name__ == '__main__':
    res = three_sum([-1, 0, 1, 2, -1, -4])
    print(res)
