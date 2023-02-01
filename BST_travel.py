"""
Time Complexity for all algorithms : O(N)
Space Complexity for all algorithms : O(N) or O(depth of tree)
"""

def inorder_traverse(tree , array):
    if tree is not None:
        inorder_traverse(tree.left , array)
        array.append(tree.value)
        inorder_traverse(tree.right , array)    
    
    return array

def pre_order_traverse(tree , array):
    if tree is not None:
        array.append(tree.value)
        pre_order_traverse(tree.left , array)
        pre_order_traverse(tree.right , array)

    return array

def post_order_traverse(tree , array):
    if tree is not None:
        post_order_traverse(tree.left , array)
        post_order_traverse(tree.right , array)
        array.append(tree.value)
    return array