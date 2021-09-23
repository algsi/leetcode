"""
264. ugly number ii

https://leetcode.com/problems/ugly-number-ii/
https://leetcode-cn.com/problems/ugly-number-ii/

丑数 II
"""

import heapq


def nth_ugly_number_v1(n: int) -> int:
    """
    最小堆

    要得到从小到大的第 n 个丑数，可以使用最小堆实现。
    初始时堆为空。首先将最小的丑数 1 加入堆。
    每次取出堆顶元素 x，则 x 是堆中最小堆丑数，由于 2x，3x，5x 也是丑数，因此将 2x，3x，5x 加入堆。
    上述做法会导致堆中出现重复元素的情况。为了避免重复元素，可以使用哈希集合去重，避免相同元素多次加入堆。
    在排除重复元素堆情况下，第 n 次从最小堆中取出的元素即为第 n 个丑数。

    时间复杂度：O(nlogn)。
    空间复杂度：O(n)。
    """
    factors = [2, 3, 5]
    seen = {1}
    heap = [1]
    for i in range(n - 1):
        cur = heapq.heappop(heap)  # 当前堆顶元素
        for factor in factors:
            nxt = cur * factor
            if nxt not in seen:
                seen.add(nxt)
                heapq.heappush(heap, nxt)

    return heapq.heappop(heap)


def nth_ugly_number_v2(n: int) -> int:
    """
    Dynamic Programming
    """
    nums = [1, ]
    i2 = i3 = i5 = 0

    for i in range(1, 1690):
        ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
        nums.append(ugly)

        if ugly == nums[i2] * 2:
            i2 += 1
        if ugly == nums[i3] * 3:
            i3 += 1
        if ugly == nums[i5] * 5:
            i5 += 1

    return nums[n - 1]
