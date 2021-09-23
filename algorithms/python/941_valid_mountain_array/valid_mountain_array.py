"""
941. valid mountain array

https://leetcode.com/problems/valid-mountain-array/
https://leetcode-cn.com/problems/valid-mountain-array/

有效的山脉数组
"""

from typing import List


def valid_mountain_array(A: List[int]) -> bool:
    """
    迭代法

    complexity analysis
    time complexity: O(N)
    space complexity: O(1)
    """
    n = len(A)
    if n < 3 or A[0] >= A[1]:
        return False
    state = True
    for i in range(2, n):
        if A[i] == A[i - 1]:
            return False
        if A[i] > A[i - 1]:
            if state:
                continue
            else:
                return False
        state = False

    return not state


def main():
    array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    r = valid_mountain_array(array)
    print(r)


if __name__ == '__main__':
    main()
