from app.main.base.node import Node 

class BinaryTreeNode(Node):
    def __init__(self, val):
        
        Node.__init__(self, val)

        self.left = None
        self.right = None

class BinaryTree:
    
    def __init__(self):
        self.root = None

    def append(self, val):
        self.root = self.insert(self.root, val)

    def insert(self, root, val):
        if not root: return BinaryTreeNode(val)     
        if val < root.val:
            if root.left: 
                root.left = self.insert(root.left, val)
            else:
                root.left = BinaryTreeNode(val)
        else:
            if root.right: 
                root.right = self.insert(root.right, val)
            else:
                root.right = BinaryTreeNode(val)
        return root

    def invert(self):
        def i(root):
            if not root:
                return None
            
            tmp = root.left
            root.left = root.right
            root.right = tmp
            i(root.left)
            i(root.right)

            return root

        return i(self.root)

    def search(self, val):

        def s(root):
            if not root:
                return None

            if val == root.val:
                return root
            
            if val < root.val:
                return s(root.left)
            else:
                return s(root.right)

        return s(self.root)

    def depth(self):

        def d(root):
            if not root:
                return 0
            return max(d(root.left), d(root.right)) + 1

        return d(self.root)
              
    def print_dfs_preorder(self):
        print("DFS RECURSIVE PRE ORDER START")
        self.dfs_preorder_recursive(self.root)
        print("DFS RECURSIVE PRE ORDER ENDS")

    def print_dfs_inorder(self):
        print("DFS RECURSIVE IN ORDER STARTS")
        self.dfs_inorder_recursive(self.root)
        print("DFS RECURSIVE IN ORDER ENDS")

        print("DFS ITERATIVE IN ORDER STARTS")
        self.dfs_inorder_iterative(self.root)
        print("DFS ITERATIVE IN ORDER ENDS")

    def print_dfs_postorder(self):
        print("DFS RECURSIVE POST ORDER START")
        self.dfs_postorder_recursive(self.root)
        print("DFS RECURSIVE POST ORDER ENDS")

    def print_bfs_tree(self):
        print("BFS STARTS")
        self.bfs()
        print("BFS ENDS")

    def print_depth(self):
        d = self.depth()
        print("DEPTH: " + str(d))

    def search_and_print(self, val):
        node = self.search(val)
        if node:
            print("FOUND: " + str(node.val))
        else:
            print("NOT FOUND: " +  str(val))
            
    def bfs(self):
        q = []
        q.append(self.root)

        while q:
            node = q.pop(0)
            self.visit(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    def dfs_preorder_recursive(self, root):
        if root:
            self.visit(root)
            self.dfs_preorder_recursive(root.left)
            self.dfs_preorder_recursive(root.right)

    def dfs_inorder_recursive(self, root):
        if root:
            self.dfs_inorder_recursive(root.left)
            self.visit(root)
            self.dfs_inorder_recursive(root.right)

    def dfs_inorder_iterative(self, root):

        current = root  
        s = []
        done = 0 
        
        while(not done): 
            if current: 
                s.append(current)         
                current = current.left  
            else: 
                if(len(s) > 0): 
                    current = s.pop() 
                    self.visit(current)
                    current = current.right  
                else: 
                    done = 1

    def dfs_postorder_recursive(self, root):
        if root:
            self.dfs_postorder_recursive(root.left)
            self.dfs_postorder_recursive(root.right)
            self.visit(root)

    def visit(self, root):
        print(root.val)