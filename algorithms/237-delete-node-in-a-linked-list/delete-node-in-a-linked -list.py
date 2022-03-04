"""
237. delete node in a linked list

删除链表中的节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: ListNode = None

    def delete_node(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
