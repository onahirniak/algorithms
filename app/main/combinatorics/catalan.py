class Catalan:

    """
    Catalan's formula for finding unique binary trees
    https://en.wikipedia.org/wiki/Catalan_number
    """
    def catalan_seq(self, n):
        C = 1.0

        for i in range(2, n + 1): 
            C = C * (n + i)/i

        return C
