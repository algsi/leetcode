from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longest_uni_value_path(root: Optional[TreeNode]) -> int:
    ans = 0

    def dfs(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        left_path = left + 1 if node.left and node.left.val == node.val else 0
        right_path = right + 1 if node.right and node.right.val == node.val else 0

        nonlocal ans
        ans = max(ans, left_path + right_path)
        return max(left_path, right_path)

    dfs(root)
    return ans
