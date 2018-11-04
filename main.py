from trees.binary_tree import BinaryTree
from trees.binary_tree_factory import BinaryTreeFactory
from lists.linked_list import LinkedList
from sorting.sorter import Sorter
from hash_tables.hash_functions import Encryption
from hash_tables.hash_table import HashTable
from graphs.graph import Graph
from arrays.array_helper import ArrayHelper
from dynamic.dynamic_programming import CoinChange
from helpers.csv_helper import CsvHelper
from os.path import dirname, abspath

def main():
    tree = BinaryTreeFactory.from_array([5,4,3,2,6,7,8,9,1])
    #tree = BinaryTreeFactory.from_random(30)

    tree.print_dfs_preorder();
    tree.print_dfs_inorder();
    tree.print_dfs_postorder();

    tree.print_bfs_tree();

    tree.print_depth()

    tree.search_and_print(5)
    tree.search_and_print(1)
    tree.search_and_print(100)

    tree.invert()

    tree.print_dfs_inorder()

    linked_list = LinkedList()

    linked_list.push(0)
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.push(0)

    linked_list.printList()

    linked_list.reverse()

    linked_list.printList()

    linked_list.search_and_print(1)
    linked_list.search_and_print(0)
    linked_list.search_and_print(100)

    linked_list.remove(3)
    linked_list.remove(0)
    linked_list.remove(0)
    linked_list.remove(0)
    linked_list.printList()

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

    hash_table = HashTable()

    hash_table.put("key", 123)
    hash_table.put("key", 1235)
    value_1 = hash_table.get("key")
    print("VALUE 1 FROM HASH TABLE: " + str(value_1))

    hash_table.put("key2", 1234)
    value_2 = hash_table.get("key2")
    print("VALUE 2 FROM HASH TABLE: " + str(value_2))

    g = Graph()

    g.add_edge(0, 1) 
    g.add_edge(0, 2) 
    g.add_edge(1, 2) 
    g.add_edge(2, 0) 
    g.add_edge(2, 3) 
    g.add_edge(3, 3)

    print("GRAPH BFS")

    g.bfs(2)

    print("")

    print("GRAPH DFS")

    g.dfs(2)

    print("")

    g = Graph()

    g.add_edge("A", "B", 7)
    g.add_edge("A", "D", 5)
    g.add_edge("B", "C", 8)
    g.add_edge("B", "D", 9)
    g.add_edge("B", "E", 7)
    g.add_edge("C", "E", 5)
    g.add_edge("D", "E", 15)
    g.add_edge("D", "F", 6)
    g.add_edge("E", "F", 8)
    g.add_edge("E", "G", 9)
    g.add_edge("F", "G", 11)    

    print("Dijkstra")
    print(g.graph)
    print("A -> E:")
    print(g.shortest_path("A", "E"))
    print("F -> G:")
    print(g.shortest_path("F", "G"))

    helper = ArrayHelper()

    array = [1,2,3,4,5,6,7,8,9]

    print("ARRAY BINARY SEARCH")

    index = helper.binary_search(array, 8)

    print(index)

    coin_change = CoinChange()

    print("COIN CHANGE")

    c = coin_change.minCoins(19, [9,6,5,1])

    print(c)

    csvHelper = CsvHelper()

    path = abspath('data.csv')
    data = csvHelper.read_csv(path)

    print(data)

    
if __name__ == '__main__':
    main()
    