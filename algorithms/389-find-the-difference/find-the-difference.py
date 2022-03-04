"""
389. find the difference

https://leetcode.com/problems/find-the-difference/
https://leetcode-cn.com/problems/find-the-difference/

找不同
"""


def find_the_difference(s: str, t: str) -> str:
    """
    位运算：异或运算

    complexity analysis
    time complexity: O(n)
    space complexity: O(1)
    """
    tmp = 0
    for i in s:
        tmp ^= ord(i)
    for j in t:
        tmp ^= ord(j)
    return chr(tmp)


def find_the_difference_2():
    """
    count

    complexity analysis
    time complexity: O(n)
    space complexity: O(n)
    """
    count = [0] * 26
    pass


def find_the_difference_3(s: str, t: str):
    """
    sum

    complexity analysis
    time complexity: O(n)
    space complexity: O(1)
    """
    tmp = 0
    for i in t:
        tmp += ord(i)
    for i in s:
        tmp -= ord(i)
    return chr(tmp)


if __name__ == '__main__':
    print(find_the_difference('abcd', 'abcde'))
