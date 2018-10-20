import unittest
from hash_tables.hash_functions import Encryption

class EncryptionTests(unittest.TestCase):

    def should_have_same_hash_for_string(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32("lol")
        hash_2 = encryption.fnv1a_32("lol")

        self.assertEqual(hash_1, hash_2)
    
    def should_have_different_hash_for_string(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32("lol")
        hash_2 = encryption.fnv1a_32("lolo")

        self.assertNotEqual(hash_1, hash_2)

    def should_have_same_hash_for_integer(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32(2030032)
        hash_2 = encryption.fnv1a_32(2030032)

        self.assertEqual(hash_1, hash_2)
    
    def should_have_different_hash_for_integer(self):
        encryption = Encryption()
        
        hash_1 = encryption.fnv1a_32(2030032)
        hash_2 = encryption.fnv1a_32(2030031)

        self.assertNotEqual(hash_1, hash_2)

class TestStringMethods(unittest.TestCase):
    
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()