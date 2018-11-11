from .sorter import Sorter

class SortingRunner():
    @staticmethod
    def run():
        sorter = Sorter()

        print("SELECTION SORT")
        array = [9,8,7,6,5,4,3,2,1]
        sorter.selection_sort(array)
        print (' '.join(str(n) for n in array))

        print("BUBBLE SORT")
        array = [9,8,7,6,5,4,3,2,1]
        sorter.selection_sort(array)
        print (' '.join(str(n) for n in array))

        print("INSERTION SORT")
        array = [9,8,7,6,5,4,3,2,1]
        sorter.selection_sort(array)
        print (' '.join(str(n) for n in array))
