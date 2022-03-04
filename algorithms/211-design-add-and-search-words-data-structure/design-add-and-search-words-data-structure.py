"""
211. design add and search words data structure

添加与搜索单词 - 数据结构设计
"""


class TrieNode:
    def __init__(self, val=None, next=None, end=False):
        if next is None:
            next = []
        self.val = val
        self.next = {i.val: i for i in next}
        self.end = end


class WordDictionary:
    """
    TrieNode + dict
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for w in word:
            if w in node.next:
                # find it
                node = node.next[w]
            else:
                node.next[w] = TrieNode(w)
                node = node.next[w]
        node.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.__backtrack(0, word, self.root)

    def __backtrack(self, index: int, word: str, node: TrieNode) -> bool:
        char = word[index]
        if char != '.':
            if index == len(word) - 1:
                return char in node.next and node.next[char].end
            if char not in node.next:
                return False
            return self.__backtrack(index + 1, word, node.next[char])

        # 通配符，需要回溯搜索
        for next_node in node.next.values():
            if index == len(word) - 1:
                if next_node.end:
                    # 如果在当前这个 index 下查找失败，还可以尝试下一个 index
                    return True
                else:
                    continue
            if self.__backtrack(index + 1, word, next_node):
                # 如果回溯搜索失败，则尝试下一个，不直接退出
                return True

        return False
