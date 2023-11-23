"""
590. n-ary-tree-postorder-traversal

N 叉树的后序遍历
"""

from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def postorder(root: Node) -> List[int]:
    """
    递归
    """
    if root is None:
        return []
    if not root.children:
        return [root.val]

    ans = []
    for ch in root.children:
        ans.extend(postorder(ch))
    ans.append(root.val)
    return ans
