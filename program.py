from trees.binary_tree import BinaryTree
from trees.binary_tree_factory import BinaryTreeFactory
from lists.linked_list import LinkedList
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



if __name__ == '__main__':
    main()
    