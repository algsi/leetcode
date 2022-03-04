"""
128 longest consecutive sequence

最长连续序列
"""

from typing import List


def longest_consecutive(nums: List[int]) -> int:
    """
    我们考虑枚举数组中的每个数 x，考虑以其为起点，不断尝试匹配 x+1,x+2,... 是否存在，假设最长匹配到 x+y，那么以
    x 为起点的最长序列即为 x+1,x+2,....,x+y，长度为 y+1，我们不断枚举更新答案即可。

    对于匹配的过程，暴力的方法是 O(n) 遍历数组去看是否存在这个数，但其实更高效的方法是用一个哈希表存储数组中的数，
    这样查看一个数是否存在即能优化至 O(1) 的时间复杂度。
    """
    num_set = {n for n in nums}
    ret = 0
    for n in num_set:
        if n - 1 not in num_set:
            seq_count = 1
            while n + seq_count in num_set:
                seq_count += 1
            if seq_count > ret:
                ret = seq_count
    return ret


if __name__ == '__main__':
    longest_consecutive([100, 4, 200, 1, 3, 2])
