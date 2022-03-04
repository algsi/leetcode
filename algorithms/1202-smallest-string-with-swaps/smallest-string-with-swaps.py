"""
1202. smallest string with swaps

https://leetcode.com/problems/smallest-string-with-swaps/
https://leetcode-cn.com/problems/smallest-string-with-swaps/

交换字符串中的元素
"""

from typing import List
import collections


class Solution:
    def smallest_string_with_swaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        union_find = UnionFind(n)
        for p, q in pairs:
            union_find.union(p, q)

        # key：连通分量的代表元，value：同一个连通分量的字符集合
        mp = collections.defaultdict(list)
        for i, ch in enumerate(s):
            mp[union_find.find(i)].append(ch)

        # 对集合中对字符进行排序
        for vec in mp.values():
            vec.sort(reverse=True)

        ans = list()
        for i in range(n):
            root = union_find.find(i)
            ans.append(mp[root].pop())

        return ''.join(ans)


class UnionFind:
    """
    加权路径压缩
    """

    def __init__(self, n: int):
        self.parent = [0] * n
        self.rank = [0] * n
        for i in range(n):
            self.parent[i] = i
            self.rank[i] = 1

    def find(self, x: int) -> int:
        root = x
        while root != self.parent[root]:
            root = self.parent[root]

        # path compress
        while x != root:
            tmp = self.parent[x]
            self.parent[x] = root
            x = tmp
        return root

    def union(self, p: int, q: int):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return
        if self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
            self.rank[root_p] += self.rank[root_q]
        else:
            self.parent[root_p] = root_q
            self.rank[root_q] += self.rank[root_p]


def main():
    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    solution = Solution()
    r = solution.smallest_string_with_swaps(s, pairs)


if __name__ == '__main__':
    main()
