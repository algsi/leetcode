"""
127. word ladder

http://leetcode.com/problems/word-ladder/submissions/
http://leetcode-cn.com/problems/word-ladder/submissions/

单词接龙
"""

from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_id_dict = dict()  # the dict for word to its id
        node_num = 0  # 节点的数量
        edge = []  # 邻接矩阵

        def add_edge(word: str):
            """
            add edge to the graph
            """
            add_word(word)
            id1 = word_id_dict[word]
            array = list(word)
            length = len(word)
            for i in range(length):
                tmp = array[i]
                array[i] = '*'  # replace
                new_word = ''.join(array)
                add_word(new_word)
                id2 = word_id_dict[new_word]

                # connect
                edge[id1].append(id2)
                edge[id2].append(id1)

                array[i] = tmp

        def add_word(word: str):
            """
            add a word to the graph
            """
            if word not in word_id_dict:
                nonlocal node_num
                word_id_dict[word] = node_num
                node_num += 1
                edge.append([])

        for word in wordList:
            add_edge(word)
        add_edge(beginWord)
        if endWord not in word_id_dict:
            return 0

        # BFS
        dis = [-1 for _ in range(node_num)]
        begin_id = word_id_dict[beginWord]
        end_id = word_id_dict[endWord]
        dis[begin_id] = 0

        queue = deque()
        queue.append(begin_id)
        while queue:
            cur = queue.popleft()
            if cur == end_id:
                return dis[cur] // 2 + 1
            for i in edge[cur]:
                if dis[i] == -1:
                    # 该节点尚未遍历
                    dis[i] = dis[cur] + 1
                    queue.append(i)
        return 0
