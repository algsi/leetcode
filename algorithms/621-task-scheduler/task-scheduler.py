"""
621. task scheduler

https://leetcode.com/problems/task-scheduler/
https://leetcode-cn.com/problems/task-scheduler/

任务调度器
"""

from typing import List


def least_interval(tasks: List[str], n: int) -> int:
    """
    设计

    尽早安排出现次数较多的任务
    """
    map = [0] * 26

    base = ord('A')
    for task in tasks:
        map[ord(task) - base] += 1

    map.sort()
    max_val = map[-1] - 1
    idle_slots = max_val * n
    for i in range(24, -1, -1):
        idle_slots -= map[i]

    return idle_slots + len(tasks) if idle_slots > 0 else len(tasks)


def main():
    tasks = ["A", "A", "A", "B", "B", "B"]
    print(least_interval(tasks, 2))


if __name__ == '__main__':
    main()
