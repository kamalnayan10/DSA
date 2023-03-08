"""
Implementing the Bredth First Seearch (BFS) Algorithm
"""



class Node:
    def __int__(self , name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    # Time O(vertices + edges) | Space O(vertices)
    def bredth_first_search(self , array):
        q = [self]

        while q:
            curr = q.pop(0)
            array.append(curr.name)

            for child in curr.children:
                q.append(child)

        return array
