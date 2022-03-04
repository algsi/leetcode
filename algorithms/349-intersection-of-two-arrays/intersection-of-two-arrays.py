"""
349. intersection of two arrays

两个数组的交集
"""

from typing import List


class Solution:

    def intersection1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        方法一：双指针
        先对两个数组进行排序，再设置两个数组的指针，在相等的时候同时后移，如果不相等，谁小谁自增，你追我赶，遍历完任何一个数组，那么就可以结束。
        """
        nums1.sort()
        nums2.sort()

        n1, n2 = len(nums1), len(nums2)
        result = []
        i, j = 0, 0
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                result.append(nums1[i])
                while True:
                    i += 1
                    if i == n1:
                        return result
                    if nums1[i] != result[-1]:
                        break
                while True:
                    j += 1
                    if j == n2:
                        return result
                    if nums2[j] != result[-1]:
                        break

        return result

    def intersection2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        方法二：两个set
        """
        set1 = set(nums1)
        set2 = set(nums2)
        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

    def set_intersection(self, set1, set2):
        return [i for i in set1 if i in set2]

    def intersection3(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        方法三：内置函数
        在 Python 中提供了交集的操作，在 Java 提供了 retainAll() 函数.
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set1 & set2)
