"""
117. populating next right pointers in each node ii

see also: 116

填充每个节点的下一个右侧节点指针 II
"""

from collections import deque


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution2:
    """
    Queue（层序遍历迭代）

    complexity analysis
    time complexity: O(n)
    space complexity: O(n)
    """

    def connect(self, root: Node) -> Node:
        if root is None:
            return root

        queue = deque([root])
        count = 1
        while queue:
            dummy = Node()
            while count:
                node = queue.popleft()
                dummy.next = node
                dummy = node

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                count -= 1

            count = len(queue)

        return root


class Solution:
    """
    使用已建立的 next 指针。已经建立起来的 next 指针实际上就构成了一个链表，前面用队列的方式就是为了便于我们遍历每一层，而现在，
    就可以利用已经建立的 next 指针（链表）来遍历每一层，这样就省去了队列的空间。

    迭代：利用每一层建立起来的链表来取代队列

    这样做的关键就是遍历每一层的时候，先构造好下一层的 next 指针，即链表

    complexity analysis
    time complexity: O(n)
    space complexity: O(1)
    """

    last: 'Node' = None  # 链表的最后一个节点
    next_start: 'Node' = None  # start of the next linked list

    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None

        start = root
        while start:
            Solution.last = None
            Solution.next_start = None
            # 遍历当前层的链表
            while start is not None:
                # left node
                if start.left:
                    self.handle(start.left)
                # right node
                if start.right:
                    self.handle(start.right)

                start = start.next

            start = Solution.next_start

        return root

    @staticmethod
    def handle(node: 'Node'):
        """
        将当前节点并入链表中
        """
        # linked to the linked list
        if Solution.last is not None:
            Solution.last.next = node

        Solution.last = node

        # update the start of the next liked list
        if Solution.next_start is None:
            Solution.next_start = node
