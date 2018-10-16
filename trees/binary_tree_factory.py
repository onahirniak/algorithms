from base.node import Node
from .binary_tree import BinaryTree
from random import randint

class BinaryTreeFactory:
    @staticmethod
    def from_array(array):
        tree = BinaryTree()
        for item in array:
            tree.append(item)
        return tree
    
    @staticmethod
    def from_random(size):
        tree = BinaryTree()
        for _ in range(size):
            n = randint(0, size);
            tree.append(n)
        return tree