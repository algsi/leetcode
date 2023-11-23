"""
326. power of three

https://leetcode.com/problems/power-of-three/
https://leetcode-cn.com/problems/power-of-three/

3的幂
"""


def is_power_of_three(n: int) -> bool:
    while n and n % 3 == 0:
        n //= 3
    return n == 1


if __name__ == '__main__':
    res = is_power_of_three(27)
    print(res)

    res = is_power_of_three(45)
    print(res)
