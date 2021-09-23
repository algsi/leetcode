"""
236. lowest common ancestor of a binary tree

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/

二叉树的最近公共祖先（LCA）
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    递归 DFS

    complexity analysis
    time complexity: O(N)
    space complexity: O(N)
    """

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == p or root == q:
            return root

        # 去左子树寻找 LCA
        left = self.lowest_common_ancestor(root.left, p, q)
        # 去右子树寻找 LCA
        right = self.lowest_common_ancestor(root.right, p, q)
        if not left:
            return right
        if not right:
            return left
        return root


class Solution2:
    """
    递归 DFS

    complexity analysis
    time complexity: O(N)
    space complexity: O(N)
    """

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None

        def dfs(node: TreeNode):
            """
            DFS the tree

            :return f(node), true indicate that the node's subtree contains p or q
            """
            if node is None:
                return False
            l_son = dfs(node.left)  # f(left_son)
            r_son = dfs(node.right)  # f(right_son)
            if (l_son and r_son) or ((node.val == p.val or node.val == q.val) and (l_son or r_son)):
                nonlocal ans
                # find the lca
                ans = node

            return l_son or r_son or node.val == p.val or node.val == q.val

        dfs(root)
        return ans


class Solution3:
    """
    用哈希表存储所有节点的父节点

    我们可以用哈希表存储所有节点的父节点，然后我们就可以利用节点的父节点信息从 p 结点开始不断往上跳，并记录已经访问过的节点，
    再从 q 节点开始不断往上跳，如果碰到已经访问过的节点，那么这个节点就是我们要找的最近公共祖先。

    1. 所有节点的值都是唯一的
    2. p、q 为不同节点且均存在于给定的二叉树中

    complexity analysis
    time complexity: O(N)
    space complexity: O(N)
    """

    def lowest_common_ancestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parent = dict()
        visited = set()

        def dfs(node: TreeNode):
            if node.left:
                parent[node.left.val] = node
                dfs(node.left)
            if node.right:
                parent[node.right.val] = node
                dfs(node.right)

        dfs(root)
        while p:
            visited.add(p)
            p = parent[p.val]
        while q:
            if parent[q.val] in visited:
                return q
            q = parent[q.val]

        return None
