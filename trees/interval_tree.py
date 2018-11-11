from .binary_tree import BinaryTreeNode

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class IntervalTreeNode(BinaryTreeNode):
    def __init__(self, interval):

        if type(interval) is not Interval:
            raise ValueError('You should pass Interval as a class.')

        BinaryTreeNode.__init__(interval)

        self.max = interval.end

class IntervalTree():
    def __init__(self):
        self.root = None

    def append(self, interval):
        return self.insert(self.root, interval)

    def insert(self, root, interval):
        if not root:
            return IntervalTreeNode(interval)

        start = root.val.start

        if interval.start < start:
            root.left = self.insert(root.left, interval)
        else:
            root.right = self.insert(root.right, interval)
    
        if root.max < interval.end:
            root.max = interval.end
        
        return root;

    def dfs_inorder_iterative(self):
    
        current = self.root  
        s = []
        done = 0 
        
        while(not done): 
            if current: 
                s.append(current)         
                current = current.left  
            else: 
                if(len(s) > 0): 
                    current = s.pop() 
                    print("START: " + current.val.start + " END: " + current.val.end + " MAX: " + current.max)
                    current = current.right  
                else: 
                    done = 1