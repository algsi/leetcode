"""
268. missing number

https://leetcode.com/problems/missing-number/
https://leetcode-cn.com/problems/missing-number/

缺失数字
"""

from typing import List


def missing_number_1(nums: List[int]) -> int:
    """
    方法一：排序
    如果数组是有序的，那么就很容易知道缺失的数字是哪个了。
    """
    nums.sort()

    # ensure that n is at the last index
    if nums[-1] != len(nums):
        return len(nums)
        # Ensure that 0 is at the first index
    elif nums[0] != 0:
        return 0

    # If we get here, then the missing number is on the range (0, n)
    for i in range(1, len(nums)):
        expected_num = nums[i - 1] + 1
        if nums[i] != expected_num:
            return expected_num


def missing_number_2(nums: List[int]) -> int:
    """
    方法二：哈希表
    """
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number


def missing_number_3(nums: List[int]) -> int:
    """
    方法三：位运算
    """
    missing = len(nums)
    for i, num in enumerate(nums):
        missing ^= (i ^ num)

    return missing


def missing_number_4(nums: List[int]) -> int:
    """
    方法四：数学方法，等差数列求和
    """
    expected_sum = len(nums) * (len(nums) + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


if __name__ == '__main__':
    print(missing_number_4([3, 0, 1]))
