"""
60 permutation sequence

第 k 个排列
"""


def get_permutation(n: int, k: int) -> str:
    factorial = [1]
    for i in range(1, n):
        factorial.append(factorial[-1] * i)

    return ''


def main():
    r = get_permutation(3, 3)
    print(r)


if __name__ == '__main__':
    main()
