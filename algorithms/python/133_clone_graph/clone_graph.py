"""
133. clone graph

克隆图
"""

import copy


class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution1:
    def clone_graph(self, node: Node) -> Node:
        if node:
            return copy.deepcopy(node)


class Solution2:
    """
    DFS
    """
    def cloneGraph(self, node: Node) -> Node:
        dic = {}

        def dfs(old: Node):
            if old not in dic:
                # 每遍历一个节点就创建一个它的副本到哈希表
                dic[old] = new = Node(old.val, None)
                # 当所有节点进入哈希表之时开始回溯，修改邻居
                new.neighbors = [*map(dfs, old.neighbors)]
            return dic[node]

        return dfs(node)


def main():
    pass


if __name__ == '__main__':
    main()
