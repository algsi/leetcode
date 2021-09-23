"""
109. convert sorted list to binary search tree

有序链表转换二叉搜索树
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: ListNode = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: TreeNode = left
        self.right: TreeNode = right


class Solution1:
    """
    分治
    """

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def get_median(left: ListNode, right: ListNode) -> ListNode:
            """
            快慢指针查找单链表的中点
            """
            fast = slow = left
            while fast != right and fast.next != right:
                fast = fast.next.next
                slow = slow.next
            return slow

        def build_tree(left: ListNode, right: ListNode) -> TreeNode:
            """
            Returns a binary search tree build with the ListNode between left (inclusive) and right (exclusive)
            """
            if left == right:
                return None
            mid = get_median(left, right)
            root = TreeNode(mid.val)
            root.left = build_tree(left, mid)
            root.right = build_tree(mid.next, right)
            return root

        return build_tree(head, None)
