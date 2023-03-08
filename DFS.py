"""
Implementing the Depth First Seearch (DFS) Algorithm
"""

class Node:
    def __int__(self , name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    # Time O(vertices + edges) | Space O(vertices)
    def depth_first_search(self , array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array
