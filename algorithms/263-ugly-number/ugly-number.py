"""
263. ugly number

https://leetcode.com/problems/ugly-number/
https://leetcode-cn.com/problems/ugly-number/


丑树
"""


def is_ugly(num: int) -> bool:
    """
     任何一个丑数都可以写成 n = 2^i * 3^j * 5^k

     控制好终止条件即可
    """
    if num <= 0:
        return False
    while num % 2 == 0:
        num = num // 2
    while num % 3 == 0:
        num = num // 3
    while num % 5 == 0:
        num = num // 5
    return num == 1
