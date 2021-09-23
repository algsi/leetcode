"""
287. find the duplicate number

https://leetcode-cn.com/problems/find-the-duplicate-number/

寻找重复数
"""

from typing import List


def find_duplicate(nums: List[int]) -> int:
    """
    就位法
    对于数组：[1,3,4,2,2]，我们将值为1的元素放在下标为1的位置，将值为2的元素放在下标为2的位置，
    如果碰到有一个相等的值已经占了它的位置，就找到了一个重复值
    """
    i = 0
    length = len(nums)
    while i < length:
        if nums[i] != i:
            if nums[nums[i]] == nums[i]:
                # 遇到了重复元素
                return nums[i]
            else:
                # 将该元素放置到其值对应到下标到位置
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
                continue
        else:
            i += 1


def find_duplicate_2(nums: List[int]) -> int:
    """
    快慢指针，类似于单链表找入环点
    """
    slow, fast = 0, 0
    slow = nums[slow]
    fast = nums[nums[fast]]
    while slow != fast:
        slow = nums[slow]
        fast = nums[nums[fast]]
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
