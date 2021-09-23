"""
1356. sort integers by the number of 1 bits

https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits/

根据数字二进制下 1 的数目排序
"""

from typing import List


class Solution:
    def sort_by_bits(self, arr: List[int]) -> List[int]:
        bit = [0] * 10001
        for i in arr:
            bit[i] = self.count(i)

        # lambda x: (bit[x], x) 表示前一个表达式 bit[x] 结果相同的时候，按后一个表达式 x 排序
        return sorted(arr, key=lambda x: (bit[x], x))

    @staticmethod
    def count(x: int) -> int:
        cnt = 0
        while x:
            cnt += x & 1
            x = x >> 1
        return cnt

    def sort_by_bits_2(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))


def main():
    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    solution = Solution()
    r = solution.sort_by_bits(arr)
    print(r)


if __name__ == '__main__':
    main()
