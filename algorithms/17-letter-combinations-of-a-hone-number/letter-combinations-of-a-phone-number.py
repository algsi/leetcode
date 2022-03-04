"""
17. letter combinations of a phone number

电话号码的字母组合
"""

from typing import List


def letter_combinations(digits: str) -> List[str]:
    """
    具备递归的性质
    """
    if not digits:
        return []
    key = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z'],
    }
    ans = ['']
    tmp = []
    for num in digits:
        for suf in key[num]:
            for pre in ans:
                tmp.append(pre + suf)
        ans = tmp
        tmp = []

    return ans


if __name__ == '__main__':
    r = letter_combinations('23')
    print(r)
