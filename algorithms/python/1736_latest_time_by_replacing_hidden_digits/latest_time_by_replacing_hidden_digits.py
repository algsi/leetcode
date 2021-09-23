"""
1736. latest time by replacing hidden digits

https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/
https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits/

替换隐藏数字得到的最晚时间
"""


def maximum_time(time: str) -> str:
    """
    贪心
    """
    time = list(time)
    if time[0] == '?':
        time[0] = '1' if '4' <= time[1] <= '9' else '2'
    if time[1] == '?':
        time[1] = '3' if time[0] == '2' else '9'
    if time[3] == '?':
        time[3] = '5'
    if time[4] == '?':
        time[4] = '9'
    return ''.join(time)
