"""
3. longest substring without repeating characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

无重复字符的最长子串
"""


def length_of_longest_substring(s: str) -> int:
    # 哈希集合，记录每个字符是否出现过
    occ = set()

    rk = 0  # 滑动窗口右指针
    ans = 0  # 结果

    n = len(s)

    for i in range(n):
        while rk < n and s[rk] not in occ:
            # 右指针不断向右滑动
            occ.add(s[rk])
            rk += 1

        ans = max(ans, rk - i)
        if rk >= n:
            break

        # 左指针向右移动一格，移除一个字符
        occ.remove(s[i])

    return ans
