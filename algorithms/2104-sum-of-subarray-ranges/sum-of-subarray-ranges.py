from typing import List


def sub_array_ranges(nums: List[int]) -> int:
    length = len(nums)
    result = 0
    for i in range(length):
        min_num = nums[i]
        max_num = nums[i]
        for j in range(i + 1, length):
            if nums[j] > max_num:
                max_num = nums[j]
            if nums[j] < min_num:
                min_num = nums[j]
            result += max_num - min_num
    return result
