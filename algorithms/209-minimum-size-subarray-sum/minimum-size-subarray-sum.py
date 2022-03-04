"""
209. minimum size subarray sum

长度最小的子数组
"""
from typing import List


def min_sub_array_len(s: int, nums: List[int]) -> int:
    """
    dual pointer
    """
    if not nums:
        return 0
    left, right = 0, 1
    n = len(nums)
    sub_sum = nums[0]

    if sub_sum >= s:
        return 1
    else:
        res = 0

    while right < n:
        sub_sum = sub_sum + nums[right]
        if sub_sum < s:
            right += 1
            continue

        tmp = sub_sum - nums[left]
        while tmp >= s:
            sub_sum = tmp
            left += 1
            tmp = sub_sum - nums[left]

        res = (right - left + 1) if res == 0 else min(res, right - left + 1)
        right += 1

    return res


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5, 6, 7]
    b = 7
    r = min_sub_array_len(b, a)  # expected result: 2
    print(r)
