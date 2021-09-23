"""
696. count binary substrings

https://leetcode-cn.com/problems/count-binary-substrings

计数二进制子串
"""


def count_binary_substrings_1(s: str) -> int:
    """
    按字符分组

    Complexity Analysis
    time complexity: O(N)
    space complexity: O(N)
    """
    if not s:
        return 0

    cur = s[0]
    count = [1]
    for i in s[1:]:
        if i == cur:
            count[-1] += 1
        else:
            cur = i
            count.append(1)

    n = len(count)
    ret = 0
    for i in range(n - 1):
        ret += min(count[i], count[i + 1])

    return ret


def count_binary_substrings_2(s: str) -> int:
    """
    按字符分组 optimized version

    Complexity Analysis
    time complexity: O(N)
    space complexity: O(1)
    """
    if not s:
        return 0

    cur = s[0]
    prev_count, cur_count = 0, 1
    ret = 0
    for i in s[1:]:
        if i == cur:
            cur_count += 1
        else:
            cur = i
            ret += min(prev_count, cur_count)
            prev_count = cur_count
            cur_count = 1

    ret += min(prev_count, cur_count)
    return ret


if __name__ == '__main__':
    s = '00110011'
    r = count_binary_substrings_2(s)
    print(r)
