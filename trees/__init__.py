from .binary_tree_factory import BinaryTreeFactory

class TreeRunner():
    @staticmethod
    def run():
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

if __name__ == '__main__':
    TreeRunner.run()
    