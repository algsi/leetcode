from typing import List


def search(nums: List[int], target: int) -> int:
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = (high-low)//2 + low
        num = nums[mid]
        if num == target:
            return mid
        elif num > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1
