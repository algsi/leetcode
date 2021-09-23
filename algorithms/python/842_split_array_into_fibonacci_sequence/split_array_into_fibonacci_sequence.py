"""
842. split array into fibonacci sequence

https://leetcode.com/problems/split-array-into-fibonacci-sequence/
https://leetcode-cn.com/problems/split-array-into-fibonacci-sequence/

将数组拆分成斐波那契序列
"""

from typing import List


class Solution:
    """
    回溯 + 剪枝
    """

    def split_into_fibonacci(self, S: str) -> List[int]:
        output = []
        length = len(S)
        max_num = 2 << 31 - 1

        def backtrack(index: int, sum: int, prev: int) -> bool:
            if index == length:
                return len(output) >= 3
            cur_num = 0
            for i in range(index, length):
                if i > index and S[index] == '0':
                    break
                cur_num = 10 * cur_num + int(S[i])
                if cur_num > max_num:
                    break
                if len(output) >= 2:
                    if cur_num < sum:
                        continue
                    elif cur_num > sum:
                        break
                output.append(cur_num)
                if backtrack(i + 1, prev + cur_num, cur_num):
                    return True
                else:
                    output.pop()
            return False

        backtrack(0, 0, 0)
        return output
