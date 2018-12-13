from .array_helper import ArrayHelper

class ArraysRunner():
    @staticmethod
    def run():
        helper = ArrayHelper()

        array = [1,2,3,4,5,6,7,8,9]

        print("ARRAY BINARY SEARCH")

        index = helper.binary_search(array, 8)

        print(index)

        print("SUM OF MAX SUB ARRAY")

        sub_array = helper.max_sub_array([-1,-2,5,-20,30,2,-5])
        
        print(sub_array)

