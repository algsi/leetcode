"""
1014. best sightseeing pair

最佳观光组合
"""

from typing import List


def max_score_sight_seeing_pair_1(A: List[int]) -> int:
    mvp_index = 0
    # mvp景点是对后一个景点贡献值最大对景点
    ans = A[1] + A[mvp_index] - 1
    if A[1] > A[0]:
        mvp_index = 1
    for sight_index in range(2, len(A)):
        ans = max(ans, A[sight_index] + A[mvp_index] - sight_index + mvp_index)
        # 当前景点能否成为后面景点的mvp，就看将与后面元素的距离能否转换成积分优势
        if A[sight_index] + (sight_index - mvp_index) >= A[mvp_index]:
            mvp_index = sight_index
    return ans


def max_score_sight_seeing_pair_2(A: List[int]) -> int:
    # 由 A[j] + A[i] - j + i 得到 A[j] - j 和 A[i] + i 两部分，而对于统计景点 j 答案的时候， A[j] - j 又不变，因此，等价于求
    # A[i] + i 的最大值
    ans = 0
    mx = A[0] + 0
    for sight_index in range(1, len(A)):
        ans = max(ans, mx + A[sight_index] - sight_index)
        mx = max(mx, A[sight_index] + sight_index)
    return ans


if __name__ == '__main__':
    res = max_score_sight_seeing_pair_2([4, 7, 5, 8])
    print(res)
