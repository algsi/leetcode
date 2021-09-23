"""
100. same tree

相同的树
"""
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution:
    """
    递归（深度优先搜索）

    树结构具备天然的递归特征
    """

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution2:
    """
    迭代（广度优先搜索）
    """

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        two queues
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        queue1 = collections.deque([p])
        queue2 = collections.deque([q])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False

            if left1:
                queue1.append(left1)
                queue2.append(left2)
            if right1:
                queue1.append(right1)
                queue2.append(right2)

        return not queue1 and not queue2

    def isSameTree2(self, p: TreeNode, q: TreeNode) -> bool:
        """
        use tuple
        """
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        queue = collections.deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if node1.val != node2.val:
                return False
            left1, right1 = node1.left, node1.right
            left2, right2 = node2.left, node2.right

            if (not left1) ^ (not left2):
                return False
            if (not right1) ^ (not right2):
                return False

            if left1:
                queue.append((left1, left2))
            if right1:
                queue.append((right1, right2))

        return not queue
