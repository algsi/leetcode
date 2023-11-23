"""
278. first bad version

https://leetcode.com/problems/first-bad-version/
https://leetcode-cn.com/problems/first-bad-version/

第一个错误的版本
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def first_bad_version(self, n):
        """
        binary search
        """
        lo, hi = 1, n
        while lo < hi:
            mid = (hi - lo) // 2 + lo
            if isBadVersion(mid):
                hi = mid
            else:
                lo = mid + 1

        return hi
