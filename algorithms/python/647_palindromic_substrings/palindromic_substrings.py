"""
647. palindromic substrings

回文子串
"""


def count_substrings_1(s: str) -> int:
    """
    中心扩展

    计算有多少个回文子串的最朴素方法就是枚举出所有的回文子串，而枚举出所有的回文字串又有两种思路，分别是：
    - 枚举出所有的子串，然后再判断这些子串是否是回文；
    - 枚举每一个可能的回文中心，然后用两个指针分别向左右两边拓展，当两个指针指向的元素相同的时候就拓展，否则停止拓展。

    第一种算法的时间复杂度明显是 O(n^3)

    complexity analysis
    time complexity: O(n^2)
    space complexity: O(1)
    """
    if not s:
        return 0
    n = len(s)
    ans = 0

    for i in range(2 * n - 1):
        # 中心扩展存在中心是字符或者空字符两种情况
        left = i // 2
        right = left + i % 2
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
            ans += 1

    return ans


def count_substrings_2(s: str) -> int:
    """
    Manacher 算法。Manacher 算法是在线性时间内求解最长回文子串的算法。
    """
    pass
