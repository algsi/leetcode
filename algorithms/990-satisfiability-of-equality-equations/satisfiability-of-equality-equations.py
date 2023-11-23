"""
990. satisfiability of equality equations

https://leetcode-cn.com/problems/satisfiability-of-equality-equations/

等式方程的可满足性
"""

from typing import List
from fundamentals.union_find.weighted_quick_union_path_compression_uf import WeightedQuickUnionPathCompressionUF


def equations_possible(equations: List[str]) -> bool:
    """
    并查集
    """
    uf = WeightedQuickUnionPathCompressionUF(26)
    base = ord('a')
    for eq in equations:
        if eq[1] == '=':
            # 等式，进行union
            uf.union(ord(eq[0]) - base, ord(eq[3]) - base)

    for eq in equations:
        if eq[1] == '!':
            # 不等式，进行find检查
            f1 = uf.find(ord(eq[0]) - base)
            f2 = uf.find(ord(eq[3]) - base)
            if f1 == f2:
                return False

    return True


if __name__ == '__main__':
    res = equations_possible(["f==a", "a==b", "f!=e", "a==c", "b==e", "c==f"])
    print(res)
