from .linked_list_node import LinkedListNode
from base.node_visitor import NodeVisitorFactory

class LinkedList:
    def __init__(self):
        self.root = None
        self.node_visitor_factory = NodeVisitorFactory()

    def push(self, val):
        node = LinkedListNode(val)

        node.next = self.root

        self.root = node
    
    def append(self, val):
        if self.root:
            current = self.root
            while current.next:
                current = current.next  
            current.next = LinkedListNode(val)
        else:
            self.root = LinkedListNode(val)

    def search(self, val):
        current = self.root

        while current:
            if current.val == val:
                return current
            current = current.next
        
        return None
    
    def reverse(self):
        # Initialize three pointers prev as NULL, curr as head and next as NULL.
        prev = None
        current = self.root

        # Iterate trough the linked list. In loop, do following.
        while current:
            # Before changing next of current,
            # store next node
            next = current.next
            # Now change next of current
            # This is where actual reversing happens
            current.next = prev
            # Move prev and curr one step forward
            prev = current
            current = next

        self.root = prev

    def remove(self, val):
        # (1) -> (2) -> (3)
        if not self.root:
            return False

        if self.root.val == val:
            self.root = self.root.next
            return True

        prev = None
        current = self.root
        while current:
            if current.val == val:
                prev.next = current.next
                return True
            prev = current
            current = current.next

    def printList(self):
        print("LINKED LIST STARTS")
        current = self.root
        while current:
            self.visit(current)
            current = current.next
        print("LINKED LIST ENDS")

    def search_and_print(self, val):
        node = self.search(val)

        if node:
            print("FOUND: " + str(node.val))
        else:
            print("NOT FOUND: " + str(val))

    def visit(self, node):
        visitor = self.node_visitor_factory.create()
        visitor.visit(node)