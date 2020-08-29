class Encryption(object):

    """
    Fowler–Noll–Vo hash function
    https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function
    """
    def fnv1a_32(self, key):
        FNV_prime = 16777619
        offset_basis = 2166136261

        hash = offset_basis
        for ch in str(key):
            hash ^= FNV_prime
            hash *= ord(ch)
        
        return hash