"""
50. pow n

pow(x, n)
"""


def my_pow(x: float, n: int) -> float:
    """
    自底向上的归并排序思想；减少计算次数

    complexity analysis:
    time complexity: O(logn)
    space complexity: O(1)
    """
    if n == 0:
        return 1

    if n < 0:
        x = 1 / x
        n = -n

    ans = 1
    group_value = x
    num_of_group = n

    while num_of_group > 1:
        if num_of_group & 1 == 1:  # 奇数个分组
            ans *= group_value
            num_of_group -= 1
            if num_of_group <= 1:
                continue

        # 分组的数量减半
        num_of_group = num_of_group >> 1
        group_value = group_value ** 2

    return ans * group_value


if __name__ == '__main__':
    print(my_pow(2, 10))
