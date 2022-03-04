"""
448. find all numbers disappeared in an array

找到所有数组中消失的数字
"""

from typing import List


def find_disappeared_numbers(nums: List[int]) -> List[int]:
    """
    交换，将元素放到本应该在的位置
    """
    ans = []
    i, n = 0, len(nums)
    while i < n:
        if i + 1 == nums[i]:
            i += 1
        elif nums[nums[i] - 1] == nums[i]:
            i += 1
        else:
            tmp = nums[nums[i] - 1]
            nums[nums[i] - 1] = nums[i]
            nums[i] = tmp

    for i in range(n):
        if i + 1 != nums[i]:
            ans.append(i + 1)

    return ans


def find_disappeared_numbers_2(nums: List[int]) -> List[int]:
    """
    use hash table
    """
    pass


def find_disappeared_numbers_3(nums: List[int]) -> List[int]:
    """
    标记法

    https://leetcode-cn.com/problems/missing-number/solution/que-shi-shu-zi-by-leetcode/

    Complexity Analysis
    time complexity: O(n)
    space complexity: O(1)
    """
    n = len(nums)
    for i in range(n):
        new_index = abs(nums[i]) - 1

        # 需要判断，避免负负得正
        if nums[new_index] > 0:
            nums[new_index] *= -1

    ret = []
    for i in range(n):
        if nums[i] > 0:
            ret.append(i + 1)
    return ret


if __name__ == '__main__':
    param = [4, 3, 2, 7, 8, 2, 3, 1]
    res = find_disappeared_numbers(param)
    print(res)
    res = find_disappeared_numbers_3(param)
    print(res)
