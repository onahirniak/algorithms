from .catalan import Catalan
from .combinations import Combinations

class CombyRunner():
    @staticmethod
    def run():
        catalan = Catalan()

        print("CATALAN")

        c = catalan.catalan_seq(6)

        print(c)

        combinations = Combinations()

        print("Combinations/Binomial coefficient")

        c = combinations.combination(5, 10)

        print(c)
