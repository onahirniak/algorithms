from base.node import Node

class LinkedListNode(Node):
    def __init__(self, val):
            
        Node.__init__(self, val)

        self.next = None