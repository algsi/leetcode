"""
767. reorganize string

https://leetcode.com/problems/reorganize-string/
https://leetcode-cn.com/problems/reorganize-string/

重构字符串
"""

import collections
import heapq


class Solution:
    """
    基于最大堆的贪心算法
    """

    def reorganize_string(self, S: str) -> str:
        if len(S) < 2:
            return S
        length = len(S)
        counts = collections.Counter(S)
        maxCount = max(counts.items(), key=lambda x: x[1])[1]
        if maxCount > (length + 1) // 2:
            return ''

        queue = [(-x[1], x[0]) for x in counts.items()]
        heapq.heapify(queue)
        ans = list()
        while len(queue) > 1:
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            ans.extend([letter1, letter2])
            counts[letter1] -= 1
            counts[letter2] -= 1
            if counts[letter1] > 0:
                heapq.heappush(queue, (-counts[letter1], letter1))
            if counts[letter2] > 0:
                heapq.heappush(queue, (-counts[letter2], letter2))
        if queue:
            ans.append(queue[0][1])

        return ''.join(ans)
