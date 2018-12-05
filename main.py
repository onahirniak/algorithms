from trees import TreeRunner
from lists import ListsRunner
from sorting import SortingRunner
from hash_tables import HashTableRunner
from graphs import GraphRunner
from arrays import ArraysRunner
from dynamic import DpRunner
from strings import StringsRunner
from helpers import CsvHelperRunner
from combinatorics import CombyRunner
import sys

def main():
    print("^.^")
    
    runners = {
        "trees": TreeRunner,
        "lists": ListsRunner,
        "sorting": SortingRunner,
        "hash": HashTableRunner,
        "graphs": GraphRunner,
        "arrays": ArraysRunner,
        "dp": DpRunner,
        "csv": CsvHelperRunner,
        "strings": StringsRunner,
        "comby": CombyRunner,
    }

    runned = False

    for key in runners:
        if key in sys.argv:
            runners[key].run()
            runned = True

    if not runned:
        print("Please use following arguments: " + str(runners.keys()))

if __name__ == '__main__':
    main()
    