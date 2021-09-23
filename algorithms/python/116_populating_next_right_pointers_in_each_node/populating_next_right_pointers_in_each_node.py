"""
116. populating next right pointers in each node

https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/

see also: 117

填充每个节点的下一个右侧节点指针
"""


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


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

    def connect(self, root: 'Node') -> 'Node':

        def link(node: Node):
            nonlocal next_start, last

            if node is None:
                return
            if last is None:
                next_start = last = node
            else:
                last.next = node
                last = last.next

        if root is None:
            return None

        next_start: Node = None  # 下一层的第一个节点
        last: Node = None  # 下一层链表中的迭代节点
        cur = root

        while cur or next_start:
            while cur is not None:
                link(cur.left)
                link(cur.right)
                cur = cur.next
            cur = next_start
            next_start = last = None

        return root
