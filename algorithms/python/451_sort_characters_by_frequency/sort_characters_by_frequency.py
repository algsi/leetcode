"""
451. sort characters by frequency

https://leetcode.com/problems/sort-characters-by-frequency/
https://leetcode-cn.com/problems/sort-characters-by-frequency/

根据字符出现频率排序
"""

import collections


def frequency_sort_v1(s: str) -> str:
    """
    按照出现的频率排序
    """
    counter = collections.Counter(s)
    keys = list(counter.keys())
    keys.sort(key=lambda x: counter[x], reverse=True)
    ans = ""
    for key in keys:
        ans = ans + key * counter[key]

    return ans


def frequency_sort_v2(s: str) -> str:
    """
    桶排序
    """
    counter = dict()
    max_freq = 0
    for i in s:
        counter[i] = counter.get(i, 0) + 1
        max_freq = max(max_freq, counter[i])

    # bucket sort
    buckets = [[] for _ in range(max_freq + 1)]
    for k, v in counter.items():
        buckets[v].append(k)

    ans = ''
    for i in range(max_freq, -1, -1):
        for ch in buckets[i]:
            ans += ch * i
    return ans


if __name__ == '__main__':
    r = frequency_sort_v2('tree')
    print(r)
