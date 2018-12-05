from .catalan import Catalan

class CombyRunner():
    @staticmethod
    def run():
        catalan = Catalan()

        print("CATALAN")

        c = catalan.catalan_seq(5)

        print(c)
