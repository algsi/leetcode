"""
1024. video stitching

https://leetcode.com/problems/video-stitching/
https://leetcode-cn.com/problems/video-stitching/

视频拼接
"""

from typing import List


class Solution1:
    """
    Dynamic programming

    :see https://leetcode-cn.com/problems/video-stitching/solution/shi-pin-pin-jie-by-leetcode-solution/
    """

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        dp = [0] + [float('inf')] * T
        for i in range(1, T + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)
        return -1 if dp[T] == float('inf') else dp[T]


class Solution2:
    """
    贪心

    注意到对于所有左端点相同的子区间，其右端点越远越有利。且最佳方案中不可能出现两个左端点相同的子区间。
    于是我们预处理所有的子区间，对于每一个位置 i，我们记录以其为左端点的子区间中最远的右端点，记为 maxn[i]。
    """

    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        maxn = [0] * T
        last = ret = pre = 0
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)
        for i in range(T):
            last = max(last, maxn[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        return ret
