"""
UNIQUE DEFINITION OF BST:

binary search tree (BST), also called an ordered or sorted binary tree, is a rooted binary tree data
structure with the key of each internal node being greater than all the keys in the respective node's
left subtree and less than the ones in its right subtree

"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        cur_node = self
        while True:
            if value < cur_node.value:
                if cur_node.left is None:
                    cur_node.left = BST(value)
                    break
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = BST(value)
                    break
                else:
                    cur_node = cur_node.right
        return self

    def contains(self, value):
        # Write your code here.
        cur_node = self
        while cur_node is not None:
            if value < cur_node.value:
                cur_node = cur_node.left
            elif value > cur_node.value:
                cur_node = cur_node.right
            else:
                return True
        return False

    def remove(self , value:int , parentNode = None):
        cur_node = self

        while cur_node is not None:
            if value < cur_node.value:
                parentNode = cur_node
                cur_node = cur_node.left
            elif value > cur_node.value:
                parentNode = cur_node
                cur_node = cur_node.right
            else:
                if cur_node.left is not None and cur_node.right is not None:
                    cur_node.value = cur_node.right.get_min_value()
                    cur_node.right.remove(cur_node.value , cur_node)

                elif parentNode is None:
                    if cur_node.left is not None:
                        cur_node.value = cur_node.left.value
                        cur_node.right = cur_node.left.right
                        cur_node.left = cur_node.left.left
                    elif cur_node.right is not None:
                        cur_node.value = cur_node.right.value
                        cur_node.left = cur_node.right.left
                        cur_node.right = cur_node.right.right
                    else:
                        pass

                elif parentNode.left == cur_node:
                    parentNode.left = cur_node.left if cur_node.left is not None else cur_node.right
                
                elif parentNode.right == cur_node:
                    parentNode.right = cur_node.left if cur_node.left is not None else cur_node.right
                
                break

        return self

    def get_min_value(self):
        cur_node = self
        while cur_node.left is not None:
            cur_node = cur_node.left
        return cur_node.value