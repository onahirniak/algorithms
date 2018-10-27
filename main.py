from trees.binary_tree import BinaryTree
from trees.binary_tree_factory import BinaryTreeFactory
from lists.linked_list import LinkedList
from sorting.sorter import Sorter
from hash_tables.hash_functions import Encryption
from hash_tables.hash_table import HashTable
from graphs.graph import Graph

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

    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)

    print("GRAPH BFS")

    g.bfs(2)

    print("")

    print("GRAPH DFS")

    g.dfs(2)

    print("")

    g = Graph({'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']})

    print("FIND PATH")

    path = g.find_path('A', 'D')

    print(path)

    print("FIND ALL PATHS")

    paths = g.find_all_paths('A', 'D')

    print(paths)

    print("FIND SHORTEST PATH")

    path = g.find_shortest_path('A', 'D')

    print(path)
    

if __name__ == '__main__':
    main()
    