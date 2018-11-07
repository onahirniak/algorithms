class StringHelper():

    def rabin_karp(self, text, sub_str):
        hs, shs, n, m = hash(text), hash(sub_str), len(text), len(sub_str)
        
        for i in range(n - m + 1):
            if hs == shs:
                if text[i:i+m] == sub_str: 
                    return [i, i+m]
            hs = hash(text[i+1:i+m+1])
        
        return []