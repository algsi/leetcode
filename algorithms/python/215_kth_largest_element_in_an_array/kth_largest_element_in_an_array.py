"""
215. kth largest element in an array

https://leetcode.com/problems/kth-largest-element-in-an-array/
https://leetcode-cn.com/problems/kth-largest-element-in-an-array/

数组中的第K个最大元素
"""

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        分治策略：快速排序

        时间复杂度：O(n)
        空间复杂度：O(logn)，递归使用栈空间的空间代价
        """
        n = len(nums)
        lo, hi = 0, n - 1
        if lo == hi:
            return nums[lo]
        p = self.__random_partition(nums, lo, hi)
        while k != p + 1:
            if k > p + 1:
                lo = p + 1
            else:
                hi = p - 1

            if lo == hi:
                return nums[lo]
            p = self.__random_partition(nums, lo, hi)

        return nums[p]

    @staticmethod
    def __random_partition(nums: List[int], lo, hi) -> int:
        """
        random select a element as a base element
        """
        pivot_id = random.randint(lo, hi)
        pivot = nums[pivot_id]
        # swap
        nums[hi], nums[pivot_id] = nums[pivot_id], nums[hi]
        # dual pointer
        i = lo - 1
        for j in range(lo, hi):
            # 注意：逆序排列
            if nums[j] >= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        # now, [lo, i - 1] less than or equal pivot, [i + 1, hi] greater than pivot
        return i

    @staticmethod
    def __partition(nums: List[int], lo, hi) -> int:
        """
        快排的partition函数，选取第一个元素作为基准元素，逆序快排

        lo != hi
        """
        i, j = lo, hi + 1
        compare = nums[lo]
        while True:
            i += 1
            j -= 1

            # find item on lo to swap
            while nums[i] >= compare:
                if i == hi:
                    break
                else:
                    i += 1
            # find item on lo to swap
            while nums[j] <= compare:
                if j == lo:
                    break
                else:
                    j -= 1

            # check if pointer cross
            if i >= j:
                break

            nums[i], nums[j] = nums[j], nums[i]

        nums[lo], nums[j] = nums[j], nums[lo]

        return j


def main():
    solution = Solution()
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    r = solution.findKthLargest(nums, k)
    print(r)


if __name__ == '__main__':
    main()
