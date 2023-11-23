"""
105. 从前序与中序遍历序列构造二叉树
"""

from logging import root
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    i = 0
    while i < len(inorder):
        if inorder[i] == preorder[0]:
            break
        else:
            i += 1
    # 递归构建
    left_count = i
    root.left = build_tree(preorder[1:left_count+1], inorder[:i])
    root.right = build_tree(preorder[left_count+1:], inorder[i+1:])
    return root
