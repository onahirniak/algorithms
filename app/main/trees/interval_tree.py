from .binary_tree import BinaryTreeNode

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __str__(self):
        return "start: " + str(self.start) + ";" + "end: " + str(self.end)

class IntervalTreeNode(BinaryTreeNode):
    def __init__(self, interval):

        if type(interval) is not Interval:
            raise ValueError('You should pass Interval as a class.')

        BinaryTreeNode.__init__(self, interval)

        self.max = interval.end

class IntervalTree():
    def __init__(self):
        self.root = None

    def append(self, interval):
        self.insert(self.root, interval)

    def insert(self, root, interval):
        if root:
            start = root.val.start

            if interval.start < start:
                if root.left: 
                    self.insert(root.left, interval)
                else:
                    root.left = IntervalTreeNode(interval)
            else:
                if root.right: 
                    self.insert(root.right, interval)
                else:
                    root.right = IntervalTreeNode(interval)
        
            if root.max < interval.end:
                root.max = interval.end
        else:
            self.root = IntervalTreeNode(interval)

    def find_overlap(self, interval):
        return self.__find_overlap__(self.root, interval)

    def __find_overlap__(self, root, interval):
        if not root: return None

        if self.__is_overlap__(root.val, interval):
            return root.val
        
        if root.left and root.left.max >= interval.start:
            return self.__find_overlap__(root.left, interval)

        return self.__find_overlap__(root.right, interval)
    
    def __is_overlap__(self, i1, i2):
        return i1.start <= i2.end and i2.start <= i1.end

    def dfs_inorder_iterative(self):
    
        current = self.root  
        s = []
        done = 0 
        
        while not done: 
            if current: 
                s.append(current)         
                current = current.left  
            else: 
                if len(s) > 0: 
                    current = s.pop() 
                    print(str(current.val) + " MAX: " + str(current.max))
                    current = current.right  
                else: 
                    done = 1