"""
208. implement trie prefix tree

实现 Trie (前缀树)
"""


class TrieNode:
    def __init__(self, val=None, next=None, end=False):
        if next is None:
            next = []
        self.val = val
        self.next = {i.val: i for i in next}
        self.end = end


class Trie:
    """
    TrieNode + dict
    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
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
        Returns if the word is in the trie.
        """
        node = self.root
        for w in word:
            if w not in node.next:
                return False
            else:
                node = node.next[w]
        return node.end

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for w in prefix:
            if w not in node.next:
                return False
            else:
                node = node.next[w]
        return True
