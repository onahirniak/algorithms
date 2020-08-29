import unittest
from app.main.hash_tables.hash_functions import Encryption

class EncryptionTests(unittest.TestCase):

    def test_should_have_same_hash_for_string(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32("lol")
        hash_2 = encryption.fnv1a_32("lol")

        self.assertEqual(hash_1, hash_2)
    
    def test_should_have_different_hash_for_string(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32("lol")
        hash_2 = encryption.fnv1a_32("lolo")

        self.assertNotEqual(hash_1, hash_2)

    def test_should_have_same_hash_for_integer(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32(2030032)
        hash_2 = encryption.fnv1a_32(2030032)

        self.assertEqual(hash_1, hash_2)
    
    def test_should_have_different_hash_for_integer(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32(2030032)
        hash_2 = encryption.fnv1a_32(2030031)

        self.assertNotEqual(hash_1, hash_2)

if __name__ == '__main__':
    unittest.main()