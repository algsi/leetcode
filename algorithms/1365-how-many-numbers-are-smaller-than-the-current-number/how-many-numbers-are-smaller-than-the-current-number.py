"""
1365. how many numbers are smaller than the current number

https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/

有多少小于当前数字的数字
"""

from typing import List


class Solution:
    """
    排序法
    """

    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        data = []
        for i in range(n):
            # 排序后会打乱元素原有的顺序，因此需要记录元素的索引
            data.append((nums[i], i))
        data.sort(key=lambda x: x[0])

        ret = [0] * n

        prev = -1
        for i in range(n):
            if prev == -1 or data[i][0] != data[i - 1][0]:
                prev = i
            ret[data[i][1]] = prev

        return ret


def main():
    solution = Solution()
    nums = [6, 5, 4, 8]
    r = solution.smallerNumbersThanCurrent(nums)
    print(r)


if __name__ == '__main__':
    main()
