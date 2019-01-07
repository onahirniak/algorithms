class Combinations():

    """
    Combinations/Binomial coefficient
    https://en.wikipedia.org/wiki/Binomial_coefficient
    """
    def combination(self, k, n):
        C = 1.0

        for i in range(1, k + 1): C = C * (n - i + 1)/i

        return C;