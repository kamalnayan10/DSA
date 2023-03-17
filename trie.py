"""
My Implementation of a trie(prefix tree) in python.
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root

        for i in word:
            if i not in cur.children:
                cur.children[i] = TrieNode()
            cur = cur.children[i]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root

        for i in word:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in prefix:
            if i not in cur.children:
                return False
            cur = cur.children[i]
        return True