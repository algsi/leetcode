"""
1. two sum

https://leetcode.com/problems/two-sum/
https://leetcode-cn.com/problems/two-sum/
"""

from typing import List


class Solution:
    """
    sort + binary search
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 排序会将原来的序列打乱，不便于我们寻找原来元素的索引
        sorted_num = sorted(nums)

        cur_target = target

        def search(lo: int, hi: int):
            """
            :param lo the low border (inclusive)
            :param hi the high border (inclusive)
            """
            while lo <= hi:
                mid = (hi - lo) // 2 + lo
                if sorted_num[mid] == cur_target:
                    return mid
                elif sorted_num[mid] > cur_target:
                    hi = mid - 1
                else:
                    lo = mid + 1

            return -1

        n = len(sorted_num)
        i, j = -1, -1
        for a in range(n - 1):
            cur_target = target - sorted_num[a]
            j = search(a + 1, n - 1)
            if j != -1:
                i = a
                break

        ans = []
        for a in range(n):
            if nums[a] == sorted_num[i]:
                ans.append(a)
                continue
            if nums[a] == sorted_num[j]:
                ans.append(a)

        return ans


class Solution2:
    """
    hash table
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        由于列表中会存在相同的元素，而哈希表中的 key 是唯一的，为了避免和自己相匹配，先查找，然后插入
        """
        hashtable = dict()
        for i in range(len(nums)):
            if target - nums[i] in hashtable:
                return [hashtable[target - nums[i]], i]

            # 插入动作要在后面
            hashtable[nums[i]] = i
        return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    r = solution.twoSum(nums, target)
    print(r)


if __name__ == '__main__':
    main()
