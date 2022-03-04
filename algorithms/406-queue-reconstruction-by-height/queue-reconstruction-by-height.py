"""
406. queue reconstruction by height

https://leetcode.com/problems/queue-reconstruction-by-height/
https://leetcode-cn.com/problems/queue-reconstruction-by-height/

根据身高重建队列
"""

from typing import List


class Solution:
    def reconstruct_queue(self, people: List[List[int]]) -> List[List[int]]:
        # 排序，先按身高排序升序，当身高相等时，再按第二个值降序排序
        people.sort(key=lambda x: (x[0], -x[1]))
        print(people)
        n = len(people)
        ans = [[] for _ in range(n)]
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]:
                    spaces -= 1
                    if spaces == 0:
                        ans[i] = person
                        break
        return ans
