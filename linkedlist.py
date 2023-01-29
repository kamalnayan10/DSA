class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1) Time | O(1) Space
    def set_head(self,node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        
        self.insert_before(self.hode,node)

    # O(1) Time | O(1) Space
    def set_tail(self,node):
        if self.tail is None:
            self.set_head(node)
            return
        self.insert_after(self.tail,node)

    # O(1) Time | O(1) Space
    def insert_before(self , node, node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return 
        self.remove(node_to_insert)

        node_to_insert.prev = node.prev
        node_to_insert.next = node

        if node.prev is None:
            self.head = node_to_insert
        else:
            node.prev.next = node_to_insert
        node.prev = node_to_insert

    # O(1) Time | O(1) Space
    def insert_after(self, node,node_to_insert):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)

        node_to_insert.prev = node
        node_to_insert.next = node.next

        if node.next is None:
            self.tail = node_to_insert
        else:
            node.next.prev = node_to_insert
        node.next = node_to_insert

    # O(pos) Time | O(1) Space
    def insert_at_pos(self, pos, node_to_insert):
        if pos == 1:
            self.set_head(node_to_insert)
            return 
        node = self.head
        cur_pos = 1
        while node is not None and cur_pos != pos:
            node= node.next
            cur_pos += 1

        if node is not None:
            self.insert_before(node,node_to_insert)
        else:
            self.set_tail(node_to_insert)

    # O(N) Time | O(1) Space
    def remove_node_with_val(self,value):
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    # O(1) Time | O(1) Space
    def remove(self , node):
        if node == self.head:
            self.head = self.head.next
        
        if node == self.tail:
            self.tail == self.tail.prev

        self.remove_node_pointers(node)


    # O(N) Time | O(1) Space
    def contains_node_with_value(self , value):
        node = self.head
        while node is not None and node.value != value:
            node = node.next
        
        return node is not None
    
    def remove_node_pointers(self,node):
        if node.prev is not None:
            node.prev.next = node.next

        if node.next is not None:
            node.next.prev = node.prev

        node.prev = None
        node.next = None