"""
146. LRU cache

https://leetcode-cn.com/problems/lru-cache/

LRU缓存机制
"""
import collections


class LRUCache(collections.OrderedDict):
    """
    OrderDict：哈希表 + 双向链表
    """

    def __init__(self, capacity: int):
        super().__init__()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self:
            return -1
        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        self.put(key, value)
        if len(self) > self.capacity:
            self.popitem(last=False)


class DLinkedNode:
    """
    Double Linked List
    """

    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev: DLinkedNode = None
        self.next: DLinkedNode = None


class LRUCache2:
    """
    双向链表 + 哈希表
    """

    def __init__(self, capacity: int):
        self.cache = {}
        # 使用伪头部节点和伪尾部节点，避免繁琐的空指向判断
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # 如果key存在，先通过哈希表定位，再将其移动到头部
        node = self.cache.get(key)
        self.__move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            # 如果key不存在，创建一个节点
            node = DLinkedNode(key, value)
            self.cache[key] = node
            self.__add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                # 如果超出容量，删除双向链表的尾部节点
                removed_node = self.__remove_tail()
                removed_node.next = None
                removed_node.prev = None
                # 删除哈希表中对应的项
                self.cache.pop(removed_node.key)
                self.size -= 1

        else:
            # key存在，先通过哈希表定位，再修改 value，并移到头部
            node = self.cache.get(key)
            node.value = value
            self.__move_to_head(node)

    def __remove_node(self, node: DLinkedNode):
        """
        删除节点
        """
        node.prev.next = node.next
        node.next.prev = node.prev

    def __add_to_head(self, node: DLinkedNode):
        """
        将节点添加到头部
        """
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head

    def __move_to_head(self, node: DLinkedNode):
        """
        将节点移动到头节点
        """
        self.__remove_node(node)
        self.__add_to_head(node)

    def __remove_tail(self):
        """
        删除尾节点
        """
        node = self.tail.prev
        self.__remove_node(node)
        return node
