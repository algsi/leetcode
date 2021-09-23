"""
705. design hashset

https://leetcode.com/problems/design-hashset/
https://leetcode-cn.com/problems/design-hashset/

设计哈希集合
"""


class MyHashSet:
    """
    拉链法
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1009
        self.table = [[] for _ in range(self.buckets)]

    def hash(self, key):
        return key % self.buckets

    def add(self, key: int) -> None:
        hash_key = self.hash(key)
        if key in self.table[hash_key]:
            # already exist
            return
        self.table[hash_key].append(key)

    def remove(self, key: int) -> None:
        hash_key = self.hash(key)
        if key not in self.table[hash_key]:
            return
        self.table[hash_key].remove(key)

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return True if key in self.table[self.hash(key)] else False


if __name__ == '__main__':
    hashset = MyHashSet()
    hashset.add(100000000)
