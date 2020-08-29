
from app.main.trees import TreeRunner
from app.main.lists import ListsRunner
from app.main.sorting import SortingRunner
from app.main.hash_tables import HashTableRunner
from app.main.graphs import GraphRunner
from app.main.arrays import ArraysRunner
from app.main.dynamic import DpRunner
from app.main.strings import StringsRunner
from app.main.helpers import CsvHelperRunner
from app.main.combinatorics import CombyRunner
import sys

def run_algorithms():
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