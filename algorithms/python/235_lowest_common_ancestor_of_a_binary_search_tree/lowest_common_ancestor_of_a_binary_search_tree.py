"""
235. lowest common ancestor of a binary search tree/

二叉搜索树的最近公共祖先
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lowest_common_ancestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    ancestor = root
    while True:
        if p.val < ancestor.val and q.val < ancestor.val:
            ancestor = ancestor.left
        elif p.val > ancestor.val and q.val > ancestor.val:
            ancestor = ancestor.right
        else:
            return ancestor
