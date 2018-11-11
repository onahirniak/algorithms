from .array_helper import ArrayHelper

class ArraysRunner():
    @staticmethod
    def run():
        helper = ArrayHelper()

        array = [1,2,3,4,5,6,7,8,9]

        print("ARRAY BINARY SEARCH")

        index = helper.binary_search(array, 8)

        print(index)

