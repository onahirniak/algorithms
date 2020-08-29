from .hash_functions import Encryption

class HashTableNode(object):

    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

class HashTable(object):
    def __init__(self, size=16):
        self.size = size
        self.buckets = [None] * size
        self.encryptor = Encryption()

    def put(self, key, value):
        index = self.get_index(key);
        if self.buckets[index]:
            node = self.buckets[index]
            
            current = node

            while current.next:
                current = current.next

            if current.key != key:
                current.next = HashTableNode(key, value)
            else:
                current.value = value
        else:
            self.buckets[index] = HashTableNode(key, value)
    
    def get(self, key):
        index = self.get_index(key);
        if self.buckets[index]:
            node = self.buckets[index]
            if node.key == key:
               return node.value
            elif node.key != key and node.next:
                current = node
                while current.next:
                    if current.next.key == key:
                        return current.value
                    current = current.next
        
        return None

    def get_index(self, key):
        return self.encryptor.fnv1a_32(key) % self.size
        