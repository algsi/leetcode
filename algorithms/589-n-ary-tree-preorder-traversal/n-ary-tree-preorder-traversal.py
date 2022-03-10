"""
589 n array tree preorder traversal

N 叉树的前序遍历
"""


from collections import defaultdict
from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def preorder(root: Node) -> List[int]:
    """
    递归
    """
    ans = []

    def dfs(node: Node):
        if node is None:
            return
        ans.append(node.val)
        for ch in node.children:
            dfs(ch)
    dfs(root)
    return ans


def preorder_v2(root: Node) -> List[int]:
    """
    迭代
    """
    if root is None:
        return []
    stack = []
    ans = []
    next_index = defaultdict(int)
    node = root
    while stack or node:
        while node:
            ans.append(node.val)
            stack.append(node)
            if not node.children:
                break
            next_index[node] = 1
            node = node.children[0]
        node = stack[-1]
        i = next_index[node]
        if i < len(node.children):
            next_index[node] = i + 1
            node = node.children[i]
        else:
            stack.pop()
            del next_index[node]
            node = None
    return ans
