"""
167. two sum ii input array is sorted

两数之和 II - 输入有序数组
"""

from typing import List


class Solution:
    """
    binary search
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        while left < n:
            if left != 0 and numbers[left] == numbers[left - 1]:
                left += 1
            right = self.__binary_search(numbers, left + 1, n - 1, target - numbers[left])
            if right != -1:
                return [left + 1, right + 1]
        return [-1, -1]

    def __binary_search(self, numbers: List[int], lo: int, hi: int, target: int) -> int:
        while lo <= hi:
            mid = (lo + hi) // 2
            if numbers[mid] == target:
                return mid
            if numbers[mid] < target:
                lo = mid + 1
            else:
                hi = mid - 1

        return -1


class Solution2:
    """
    dual pointer
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1
        while left < right:
            tmp = numbers[left] + numbers[right]
            if tmp == target:
                return [left + 1, right + 1]
            if tmp > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]


if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution2()
    r = solution.twoSum(numbers, target)
    print(r)
