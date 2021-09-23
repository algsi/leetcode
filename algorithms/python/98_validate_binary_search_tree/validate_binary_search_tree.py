"""
LeetCode 98：验证二叉搜索树

https://leetcode-cn.com/problems/validate-binary-search-tree/
"""


class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: TreeNode
        self.right: TreeNode


def is_valid_bst(root: TreeNode) -> bool:
    """
    非递归验证二叉搜索树（中序遍历）
    """
    stack, in_order = [], float('-inf')
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        if node.val < in_order:
            return False
        # update the in_order value
        in_order = node.val
        node = node.right

    return True
