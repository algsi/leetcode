"""
66. plus one

加一
"""

from typing import List


def plus_one(digits: List[int]) -> List[int]:
    n = len(digits)
    for i in range(n - 1, -1, -1):
        digits[i] += 1
        digits[i] = digits[i] % 10
        if digits[i] != 0:
            return digits

    # other case: 99 or 999 ...
    digits = [0] * (n + 1)
    digits[0] = 1
    return digits


def main():
    ret = plus_one([9, 9, 9])
    print(ret)


if __name__ == '__main__':
    main()
