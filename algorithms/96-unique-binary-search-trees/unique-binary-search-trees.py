"""
96. unique binary search trees

不同的二叉搜索树
"""


def num_trees(n: int) -> int:
    """
    catalan
    """
    c = 1
    for i in range(n):
        c = c * 2 * (2 * i + 1) / (i + 2)
    return int(c)
