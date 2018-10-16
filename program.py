from trees.binary_tree import BinaryTree
from trees.binary_tree_factory import BinaryTreeFactory

def main():
    #tree = BinaryTreeFactory.from_array([5,4,3,2,6,7,8,9,1])
    tree = BinaryTreeFactory.from_random(30)

    tree.print_dfs_preorder();
    tree.print_dfs_inorder();
    tree.print_dfs_postorder();

    tree.print_bfs_tree();

    tree.print_depth()

    tree.search_and_print(5)
    tree.search_and_print(1)
    tree.search_and_print(100)


if __name__ == '__main__':
    main()
    