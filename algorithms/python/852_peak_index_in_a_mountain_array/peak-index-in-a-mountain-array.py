from typing import List


def peak_index_in_mountain_array_v1(arr: List[int]) -> int:
    """
    枚举找出最大值
    """
    n = len(arr)
    ans = -1
    for i in range(1, n - 1):
        if arr[i] > arr[i + 1]:
            ans = i
            break
    return ans


def peak_index_in_mountain_array_v2(arr: List[int]) -> int:
    """
    二分查找
    """
    n = len(arr)
    left, right , ans = 1, n - 2, 0
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans
