"""
671. second minimum node in a binary tree

https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/

二叉树中第二小的节点
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_second_minimum_value(root: TreeNode) -> int:
    """
    深度优先搜索 DFS

    root value 为根节点值，根据特性，二叉树根节点的值即为所有节点中的最小值。
    只需要找出严格大于 root value 的最小值，即为结果。·
    """
    ans, root_value = -1, root.val

    def dfs(node: TreeNode) -> None:
        nonlocal ans
        if not node:
            return
        if ans != -1 and node.val >= ans:
            return
        if node.val > root_value:
            ans = node.val
        dfs(node.left)
        dfs(node.right)

    dfs(root_value)
    return ans
