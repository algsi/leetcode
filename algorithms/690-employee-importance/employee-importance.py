"""
690. employee importance

https://leetcode.com/problems/employee-importance/
https://leetcode-cn.com/problems/employee-importance/

员工的重要性
"""

from typing import List
import collections


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class SolutionV1:
    """
    深度优先搜索
    """

    def get_importance(self, employees: List['Employee'], id: int) -> int:
        mp = {employee.id: employee for employee in employees}

        def dfs(idx: int) -> int:
            employee = mp[idx]
            total = employee.importance + sum(dfs(sub_idx) for sub_idx in employee.subordinates)
            return total

        return dfs(id)


class SolutionV2:
    """
    广度优先搜索
    """

    def get_importance(self, employees: List['Employee'], id: int) -> int:
        mp = {employee.id: employee for employee in employees}
        total = 0
        que = collections.deque([id])
        while que:
            cur_id = que.popleft()
            employee = mp[cur_id]
            total += employee.importance
            for sub_idx in employee.subordinates:
                que.append(sub_idx)

        return total
