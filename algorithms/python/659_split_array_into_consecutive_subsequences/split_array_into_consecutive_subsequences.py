"""
659. split array into consecutive subsequences

https://leetcode.com/problems/split-array-into-consecutive-subsequences/
https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences/

分割数组为连续子序列
"""

from typing import List


class Solution:
    """
    贪心算法

    对于数组中元素 x，如果存在一个子序列以 x - 1 结尾，则可以将 x 加入该子序列中。将 x 加入已有的子序列总是比新建一个只包含 x 的子序列
    更优，因为前者可以将一个已有的子序列的长度增加 1，而后者新建一个长度为 1 的子序列，而题目要求分割成的子序列长度不小于 3，
    因此应该尽量避免新建短的子序列。

    complexity analysis
    time complexity: O(n)，需要遍历数组两次。
    space complexity: O(n)，需要两个哈希表，两个哈希表的大小都不会超过 n。
    """

    def is_possible(self, nums: List[int]) -> bool:
        count_dict = dict()  # 数组中每个数字的剩余次数
        end_dict = dict()  # 数组中每个数字作为结尾的子序列数量
        for i in nums:
            count = count_dict.get(i, 0)
            count_dict[i] = count + 1
        for x in nums:
            count = count_dict[x]
            if count > 0:
                prev_end_count = end_dict.get(x - 1, 0)
                if prev_end_count > 0:
                    count_dict[x] = count - 1
                    end_dict[x - 1] -= 1
                    end_dict[x] = end_dict.get(x, 0) + 1
                else:
                    count1 = count_dict.get(x + 1, 0)
                    count2 = count_dict.get(x + 2, 0)
                    if count1 > 0 and count2 > 0:
                        # 组成一个序列
                        count_dict[x] -= 1
                        count_dict[x + 1] -= 1
                        count_dict[x + 2] -= 1
                        end_dict[x + 2] = end_dict.get(x + 2, 0) + 1
                    else:
                        return False
        return True
