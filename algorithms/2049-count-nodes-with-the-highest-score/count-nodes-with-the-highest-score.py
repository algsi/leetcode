"""
2049. count-nodes-with-the-highest-score

统计最高分的节点数目
"""


from re import S
from typing import List


def count_highest_score_nodes(parents: List[int]) -> int:
    """
    借助数组实现深度优先遍历，计算出以某个节点为根节点的树的大小。
    """
    n = len(parents)

    # build tree
    children = [[] for _ in range(n)]
    for node, p in enumerate(parents):
        if p != -1:
            children[p].append(node)

    max_score, cnt = 0, 0

    def dfs(node: int) -> int:
        """
        Deep first search. Return the size of the tree with the current node as the root node.
        """
        score = 1
        size = n - 1

        for ch in children[node]:
            sz = dfs(ch)
            score *= sz
            size -= sz
        if node != 0:
            score *= size

        nonlocal max_score, cnt
        if score == max_score:
            cnt += 1
        elif score > max_score:
            max_score = score
            cnt = 1

        return n - size
    dfs(0)
    return cnt
