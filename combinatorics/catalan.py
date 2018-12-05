class Catalan:
    def catalan_seq(self, n):
        C = 1

        for i in range(n):
            C = C * 2 * (2 * i + 1)/(i+2)

        return C
