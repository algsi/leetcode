"""
617. merge two binary trees

https://leetcode.com/problems/merge-two-binary-trees
https://leetcode-cn.com/problems/merge-two-binary-trees

合并二叉树
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        recursion

        complexity analysis
        time complexity: O(N),
        space complexity: O(N)
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        t1.val += t2.val
        # 节点更新
        t1.right = self.mergeTrees(t1.right, t2.right)  # merge right subtree
        t1.left = self.mergeTrees(t1.left, t2.left)  # merge left subtree
        return t1


class Solution2:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        """
        迭代
        """
        if t1 is None:
            return t2
        if t2 is None:
            return t1

        # 往栈 push 的顺序先 t1 树，然后 t2 树
        stack = [t1, t2]
        while len(stack) > 0:
            # merge current node
            node2 = stack.pop()
            node1 = stack.pop()
            node1.val += node2.val

            # merge the left subtree
            if node1.left is None:
                node1.left = node2.left
            elif node2.left is not None:
                stack.append(node1.left)
                stack.append(node2.left)

            # merge the left subtree
            if node1.right is None:
                node1.right = node2.right
            elif node2.right is not None:
                stack.append(node1.right)
                stack.append(node2.right)

        return t1
