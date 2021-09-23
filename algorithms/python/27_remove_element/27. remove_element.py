"""
27. remove element

https://leetcode-cn.com/problems/remove-element
https://leetcode.com/problems/remove-element

移除元素
"""

from typing import List


def remove_element(nums: List[int], val: int) -> int:
    """
    dual pointer：快慢指针
    """
    if nums is None:
        return 0

    bound = -1
    for i in range(len(nums)):
        if nums[i] != val:
            bound += 1
            if bound != i:
                nums[bound] = nums[i]

    return bound + 1
