"""
18. 4sum

https://leetcode-cn.com/problems/4sum/
https://leetcode.com/problems/4sum/

四数之和
"""

from typing import List


def solution(nums: List[int], target: int) -> List[List[int]]:
    """
    排序 + 双指针
    """
    result = []

    if not nums or len(nums) < 4:
        return result

    # 后面的操作前提是排序
    nums.sort()
    length = len(nums)

    for i in range(length - 3):
        # 当k的值与前面的值相等时忽略
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 剪枝
        # 获取从当前位置起连续取四个数得到的最小值，如果最小值比目标值大，说明后面的四数和会更大，则直接跳过
        min1 = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
        if min1 > target:
            break
        # 获取当前能得到的最大值，如果最大值比目标值小，也直接跳过
        max1 = nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1]
        if max1 < target:
            continue

        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            lo = j + 1
            hi = length - 1
            # 剪枝
            min2 = nums[i] + nums[j] + nums[lo] + nums[lo + 1]
            if min2 > target:
                continue
            max2 = nums[i] + nums[j] + nums[hi] + nums[hi - 1]
            if max2 < target:
                continue

            # 左右指针开始彼此向对方靠近，要注意去重
            while lo < hi:
                if lo > j + 1 and nums[lo] == nums[lo - 1]:
                    lo += 1
                    continue
                if hi < length - 1 and nums[hi] == nums[hi + 1]:
                    hi -= 1
                    continue

                cur = nums[i] + nums[j] + nums[lo] + nums[hi]
                if cur == target:
                    result.append([nums[i], nums[j], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1
                elif cur > target:
                    hi -= 1
                else:
                    lo += 1

    return result


if __name__ == '__main__':
    r = solution([-1, 0, 1, 2, -1, -4], -1)
    print(r)
