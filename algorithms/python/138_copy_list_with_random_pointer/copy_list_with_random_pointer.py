"""
138. copy list with random pointer

https://leetcode-cn.com/problems/copy-list-with-random-pointer/

复制带随机指针的链表

参考：https://www.cnblogs.com/zhangzhe532/p/11263136.html
"""


class Node:
    def __init__(self, x, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


def copy_random_list(head: Node) -> Node:
    """
    一次遍历 + 哈希表

    时间复杂度：O(n)
    空间复杂度：O(n)
    """
    if head is None:
        return None

    # 一个map存储节点到复制节点的映射关系
    map = {}

    dummy = Node(0, None, None)
    cur = dummy
    while head is not None:
        if head in map:
            # 从map中获取当前节点的复制节点
            tmp = map.get(head)
        else:
            # 手动复制并放入map中
            tmp = Node(head.val, None, None)
            map.setdefault(head, tmp)

        cur.next = tmp

        if head.random is not None:
            # 当前节点有随机指向，复制随机指向
            if head.random in map:
                tmp.random = map.get(head.random)
            else:
                tmp.random = Node(head.random.val, None, None)
                map.setdefault(head.random, tmp.random)
        head = head.next
        cur = tmp

    return dummy.next


def copy_random_list_2(head: Node) -> Node:
    """
     三次遍历

    时间复杂度：O(n)
    空间复杂度：O(1)
    """
    cur = head

    # 第一步：复制节点到原节点到后面
    while cur is not None:
        cur_copy = Node(cur.val, cur.next, None)
        cur.next = cur_copy
        cur = cur_copy.next

    cur = head
    # 第二步：复制随机指针到指向关系
    while cur is not None:
        # 复制随机指针指向时，原节点的随机节点的下一个节点即为新节点的随机节点
        if cur.random is not None:
            cur.next.random = cur.random.next
        cur = cur.next.next

    cur = head
    head_copy = head.next
    # 第三步：拆分链表
    while True:
        cur_copy = cur.next
        cur.next = cur_copy.next
        if cur.next is None:
            return head_copy
        else:
            cur_copy.next = cur.next.next
        cur = cur.next
