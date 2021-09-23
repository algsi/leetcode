"""
33. search in rotated sorted array

搜索旋转排序数组
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    搜索旋转排序数组(你可以假设数组中不存在重复的元素)
    二分法：获取数据的中点，把数组分成两份，这两份子数组中总有一份是有序的
    """
    if len(nums) == 0:
        return -1
    elif len(nums) == 1:
        return 0 if nums[0] == target else -1

    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (hi - lo) // 2 + lo

        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            if nums[hi] >= nums[mid + 1]:  # mid右边的子数组有序，左边不确定
                if target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:  # mid左边的子数组有序，右边不确定
                lo = mid + 1
        else:
            if nums[hi] >= nums[mid + 1]:  # mid右边的子数组有序，左边不确定
                if nums[mid] > nums[hi] and target <= nums[hi]:
                    # 特殊考虑mid处于转折点的位置
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:  # 左边的子数组有序
                if target > nums[hi]:
                    hi = mid - 1
                else:
                    lo = mid + 1

    if lo == hi:
        return hi if nums[hi] == target else -1

    return -1


if __name__ == '__main__':
    print(search([3, 4, 5, 6, 1, 2], 2))
