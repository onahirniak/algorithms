from base.node import Node

class HashTableNode(object):

    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value