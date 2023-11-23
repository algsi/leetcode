"""
1207. unique number of occurrences

独一无二的出现次数
"""

from typing import List


def unique_occurrences(arr: List[int]) -> bool:
    """
    哈希表
    """
    counter = dict()
    for i in arr:
        counter[i] = counter.get(i, 0) + 1
    times = set(counter.values())
    return len(times) == len(counter)


def main():
    arr = [1, 2, 2, 1, 1, 3]
    r = unique_occurrences(arr)
    print(r)


if __name__ == '__main__':
    main()
