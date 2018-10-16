from base.node import Node 

class BinaryTreeNode(Node):
    def __init__(self, val):
        
        Node.__init__(self, val)

        self.left = None
        self.right = None
