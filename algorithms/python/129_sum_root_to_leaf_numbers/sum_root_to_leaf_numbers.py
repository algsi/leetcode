"""
129. sum root to leaf numbers

求根到叶子节点数字之和
"""

from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Recursion

    深度优先搜索

    complexity analysis:
    time complexity: O(N)
    space complexity: O(N)
    """

    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        output = 0

        def dfs(node: TreeNode, cur_sum: int):
            cur_sum = 10 * cur_sum + node.val
            if node.left is None and node.right is None:
                # a leaf node
                nonlocal output
                output += cur_sum
                return
            if node.left:
                dfs(node.left, cur_sum)
            if node.right:
                dfs(node.right, cur_sum)

        dfs(root, 0)
        return output


class Solution2:
    """
    Traversal

    广度优先搜索

    complexity analysis:
    time complexity: O(N)
    space complexity: O(N)
    """

    def sumNumbers(self, root: TreeNode) -> int:
        """
        use queue
        """
        if root is None:
            return 0
        total = 0
        queue = deque([(root, root.val)])
        while queue:
            node, num = queue.popleft()
            left, right = node.left, node.right
            if not left and not right:
                total += num
            else:
                if left:
                    queue.append((left, num * 10 + left.val))
                if right:
                    queue.append((right, num * 10 + right.val))

        return total
