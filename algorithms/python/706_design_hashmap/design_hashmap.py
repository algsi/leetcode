"""
706. design hashmap

https://leetcode.com/problems/design-hashmap/
https://leetcode-cn.com/problems/design-hashmap/

设计哈希映射
"""


class MyHashMap:
    """
    拉链法
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket = 1009
        self.table = [[] for _ in range(self.bucket)]

    def __hash(self, key):
        return key % self.bucket

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_key = self.__hash(key)
        key_list = self.table[hash_key]
        for lst in key_list:
            if lst[0] == key:
                lst[1] = value
                return
        key_list.append([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_key = self.__hash(key)
        key_list = self.table[hash_key]
        for lst in key_list:
            if lst[0] == key:
                return lst[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_key = self.__hash(key)
        key_list = self.table[hash_key]
        for i, item in enumerate(key_list):
            if item[0] == key:
                key_list.pop(i)
                return
