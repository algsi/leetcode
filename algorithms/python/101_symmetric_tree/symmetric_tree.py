"""
101. symmetric tree

https://leetcode-cn.com/problems/symmetric-tree/
https://leetcode.com/problems/symmetric-tree/

对称二叉树
"""
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left: TreeNode = None
        self.right: TreeNode = None


def is_symmetric_1(root: TreeNode) -> bool:
    """
    递归方法
    """
    return is_mirror(root, root)


def is_mirror(left: TreeNode, right: TreeNode) -> bool:
    if left is None:
        return right is None
    elif right is None:
        return False

    return left.val == right.val and is_mirror(left.right, right.left) and is_mirror(left.left, right.right)


def is_mirror_2(root: TreeNode) -> bool:
    """
    遍历，利用队列实现BFS层序遍历，但是有些变化
    """

    # 队列中每两个连续的结点应该是相等的，而且它们的子树互为镜像
    queue = deque()
    queue.append(root)
    queue.append(root)

    while len(queue) != 0:
        # 每次提取两个结点并比较它们的值。然后，将两个结点的左右子结点按相反的顺序插入队列中。
        t1 = queue.popleft()
        t2 = queue.popleft()
        if t1 is None and t2 is None:
            continue
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False

        queue.append(t1.left)
        queue.append(t2.right)
        queue.append(t1.right)
        queue.append(t2.left)

    return True


def is_symmetric_3(root: TreeNode) -> bool:
    """
    利用中序遍历
    """
    if root is None:
        return True
    left_stack = []
    right_stack = []
    left_node = root
    right_node = root
    while left_node is not None or len(left_stack) != 0:
        while left_node is not None:
            if right_node is None or (left_node.val != right_node.val):
                return False

            left_stack.append(left_node)
            right_stack.append(right_node)
            left_node = left_node.left
            right_node = right_node.right

        left_node = left_stack.pop().right
        right_node = right_stack.pop().left

    return True
