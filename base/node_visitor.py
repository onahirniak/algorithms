class DummyNodeVisitor:
    def visit(self, node):
        print(node.val)

class NodeVisitorFactory:
    def __init__(self):
        self.default = DummyNodeVisitor()

    def create(self, type=0):
        return self.default;