"""
739. daily temperatures

https://leetcode.com/problems/daily-temperatures/
https://leetcode-cn.com/problems/daily-temperatures/

每日温度
"""

from typing import List


def daily_temperatures(T: List[int]) -> List[int]:
    if not T:
        return []
    # 栈中存索引
    stack = []
    ans = [0 for _ in range(len(T))]
    for i in range(len(T) - 1, -1, -1):
        if len(stack) == 0:
            # ans[i] = 0，初始化就是0
            stack.append(i)
        elif T[i] < T[stack[-1]]:
            # 比栈顶对应的元素要小，这是距离最近的更高的温度
            ans[i] = stack[-1] - i
            stack.append(i)
        else:
            # 比栈顶对应的元素要大或者相等，尝试出栈寻找更高的温度
            stack.pop()
            while len(stack) > 0:
                tmp = stack[-1]
                if T[i] >= T[tmp]:
                    stack.pop()
                else:
                    # 遇到一个更高的温度，记录
                    ans[i] = tmp - i
                    break
            # 无论如何，将当前温度的索引入栈
            stack.append(i)

    return ans
