import random


class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.indices = {}

    def insert(self, val: int) -> bool:
        if val in self.indices:
            return False
        self.indices[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        idx = self.indices[val]
        last = len(self.nums) - 1
        self.nums[idx] = self.nums[last]
        self.indices[self.nums[idx]] = idx
        self.nums = self.nums[:last]
        del self.indices[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)
