"""
88. merge sorted array

https://leetcode-cn.com/problems/merge-sorted-array/

合并两个有序数组
"""

from typing import List


def merge_1(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.

    归并排序原理，需要额外的存储空间（双指针 / 从前往后）

    时间复杂度 : O(n + m)
    空间复杂度 : O(m)
    """
    # make a copy of nums1
    nums1_copy = nums1[:m]
    nums1 = []
    p1, p2 = 0, 0
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # if there are still elements to add
    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    else:
        nums1[p1 + p2:] = nums2[p2:]


def merge_2(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    方法二已经取得了最优的时间复杂度O(n + m)，但需要使用额外空间。这是由于在从头改变 nums1 的值时，需要把 nums1 中的元素存放在其他位置。

    如果我们从结尾开始改写 nums1 的值又会如何呢？这里没有信息，因此不需要额外空间。
    """
    p1, p2 = m - 1, n - 1
    p = m + n - 1
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1

    # add missing elements from nums2
    nums1[:p2 + 1] = nums2[:p2 + 1]
