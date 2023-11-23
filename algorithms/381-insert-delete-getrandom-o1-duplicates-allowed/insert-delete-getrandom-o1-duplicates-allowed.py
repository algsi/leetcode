"""
381. insert delete getrandom o1 duplicates allowed

https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/
https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/

O(1) 时间插入、删除和获取随机元素 - 允许重复
"""

import random


class RandomizedCollection:
    """
    hash table
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.idx = dict()

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.nums.append(val)
        num_set = self.idx.get(val, set())
        num_set.add(len(self.nums) - 1)
        self.idx[val] = num_set
        return len(num_set) == 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.idx:
            return False
        it = iter(self.idx[val])
        i = next(it)
        last_num = self.nums[-1]
        self.nums[i] = last_num
        self.idx[val].remove(i)
        if len(self.nums) - 1 in self.idx[last_num]:
            # set remove, must be a member, otherwise raise a KeyError
            self.idx[last_num].remove(len(self.nums) - 1)
        if i < len(self.nums) - 1:
            self.idx[last_num].add(i)
        if len(self.idx[val]) == 0:
            self.idx.pop(val)
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


def main():
    rc = RandomizedCollection()
    rc.insert(1)
    rc.remove(1)
    rc.insert(1)


if __name__ == '__main__':
    main()
