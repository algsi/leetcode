"""
41. first missing positive

缺失的第一个正数
"""

from typing import List


def first_missing_positive(nums: List[int]) -> int:
    """
    将数组视为哈希表：让所有元素按自身的位置就坐，1坐到第一个位置，2坐到第二个位置
    这个思想就相当于我们自己编写哈希函数，这个哈希函数的规则特别简单，那就是数值为 i 的数映射到下标为 i - 1 的位置。
    """
    i = 0
    while i < len(nums):
        if i + 1 != nums[i]:
            # 位置不正确
            if 1 <= nums[i] <= len(nums) and nums[nums[i] - 1] != nums[i]:
                # 有该元素对应的位置并且位置被不合理的元素占用了
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
                continue

        i += 1

    for i in range(len(nums)):
        if i + 1 != nums[i]:
            return i + 1

    return len(nums) + 1


if __name__ == '__main__':
    print(first_missing_positive([1, 1]))
