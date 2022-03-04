"""
863. all nodes distance k in binary tree

https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/

二叉树中所有距离为 K 的结点
"""

from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def distance_k(root: TreeNode, target: TreeNode, k: int) -> List[int]:
    parent = dict()

    def find_parents(node: TreeNode):
        if node.left:
            parent[node.left.val] = node
            find_parents(node.left)
        if node.right:
            parent[node.right.val] = node
            find_parents(node.right)

    find_parents(root)
    ans = []

    def find_ans(node: TreeNode, source: TreeNode, depth: int):
        nonlocal ans
        if not node:
            return
        if depth == k:  # 将所有深度为 k 的结点的值计入结果
            ans.append(node.val)
        if node.left != source:
            find_ans(node.left, node, depth + 1)
        if node.right != source:
            find_ans(node.right, node, depth + 1)
        if parent.get(node.val, None) != source:
            find_ans(parent.get(node.val, None), node, depth + 1)

    find_ans(target, None, 0)
    return ans
