"""
75. sort colors

https://leetcode.com/problems/sort-colors/
https://leetcode-cn.com/problems/sort-colors/
"""

from typing import List

"""
本题是经典的荷兰国旗问题，由计算机科学家 Edsger W. Dijkstra 首先提出。
"""


def sort_colors_1(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    单指针，在第一次遍历中，将数组中所有的0都交换到数组的头部，在第二次遍历中，将数组中所有的1都交换到头部都0之后，此时数组中所有的2就自然的
    在数组尾部，这样我们就完成了排序
    """

    size = len(nums)
    ptr = 0
    for i in range(size):
        if nums[i] == 0:
            nums[ptr], nums[i] = nums[i], nums[ptr]
            ptr += 1

    for i in range(ptr, size):
        if nums[i] == 1:
            nums[ptr], nums[i] = nums[i], nums[ptr]
            ptr += 1


def sort_colors_2(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.

    双指针：p0 用来交换 0，p1 用来交换 1
    """
    size = len(nums)
    # 用来指示 0 和 1 的位置
    p0, p1 = 0, 0
    for i in range(size):
        if nums[i] == 0:
            nums[p0], nums[i] = nums[i], nums[p0]
            if p0 < p1:
                nums[p1], nums[i] = nums[i], nums[p1]
            p0 += 1
            p1 += 1
        elif nums[i] == 1:
            nums[p1], nums[i] = nums[i], nums[p1]
            p1 += 1


def sort_color_3(nums: List[int]) -> None:
    """
    双指针：p0 用来交换 0，p2 用来交换 2
    """
    size = len(nums)
    p0, p2 = 0, size - 1
    i = 0
    while i <= p2:
        while i <= p2 and nums[i] == 2:
            nums[i], nums[p2] = nums[p2], nums[i]
            p2 -= 1

        if nums[i] == 0:
            nums[i], nums[p0] = nums[p0], nums[i]
            p0 += 1

        i += 1
