from .hash_table import HashTable

class HashTableRunner():
    @staticmethod
    def run():
        hash_table = HashTable()

        hash_table.put("key", 123)
        hash_table.put("key", 1235)
        value_1 = hash_table.get("key")
        print("VALUE 1 FROM HASH TABLE: " + str(value_1))

        hash_table.put("key2", 1234)
        value_2 = hash_table.get("key2")
        print("VALUE 2 FROM HASH TABLE: " + str(value_2))
