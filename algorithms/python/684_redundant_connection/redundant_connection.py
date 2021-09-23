"""
684. redundant connection

https://leetcode-cn.com/problems/redundant-connection/

冗余连接
"""
from typing import List


class Solution:
    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        union_find = QuickUnion(n)
        for p, q in edges:
            root_p = union_find.find(p)
            root_q = union_find.find(q)
            if root_p == root_q:
                return [p, q]
            union_find.direct_union(root_p, root_q)


class QuickUnion:
    """
    路径压缩的并查集
    """

    def __init__(self, n: int):
        self.parent = [i for i in range(n + 1)]

    def find(self, x: int) -> int:
        root = self.parent[x]
        while root != self.parent[root]:
            root = self.parent[root]

        # path compression
        while x != root:
            tmp = self.parent[x]
            self.parent[x] = root
            x = tmp

        return root

    def union(self, p: int, q: int):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p != root_q:
            self.parent[root_p] = root_q

    def direct_union(self, root1: int, root2: int):
        """
        在已经两个根节点的情况下，直接合并
        """
        self.parent[root1] = root2
