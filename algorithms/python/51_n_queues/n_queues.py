"""
51. n queues

https://leetcode.com/problems/n-queens/
https://leetcode-cn.com/problems/n-queens/
"""

from typing import List


class Solution:
    """
    回溯法
    """

    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(t: int):
            if t == n:
                # a solution
                solution = []
                for i in range(n):
                    s = ['.'] * n
                    s[place[i]] = 'Q'
                    solution.append(''.join(s))
                output.append(solution)
                return

            for i in range(n):
                place[t] = i

                flag = True
                # check the place
                for j in range(t):
                    # 两个在不同行上的皇后是否处在不同列以及不处于斜线上
                    if place[t] == place[j] or abs(t - j) == abs(place[t] - place[j]):
                        flag = False
                        break

                if flag:
                    backtrack(t + 1)

        place = [0] * n  # 记录每个皇后所在的位置（列索引）
        output = []
        backtrack(0)
        return output
