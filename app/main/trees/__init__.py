from app.main.trees.binary_tree_factory import BinaryTreeFactory
from app.main.trees.interval_tree import IntervalTree, Interval

class TreeRunner():
    @staticmethod
    def run():
        tree = BinaryTreeFactory.from_array([5,4,3,2,6,7,8,9,1])
        #tree = BinaryTreeFactory.from_random(30)

        tree.print_dfs_preorder()
        tree.print_dfs_inorder()
        tree.print_dfs_postorder()

        tree.print_bfs_tree()

        tree.print_depth()

        tree.search_and_print(5)
        tree.search_and_print(1)
        tree.search_and_print(100)

        tree.invert()

        tree.print_dfs_inorder()


        print("INTERVAL TREE")

        interval_tree = IntervalTree()
        interval_tree.append(Interval(1,4))
        interval_tree.append(Interval(1,3))
        interval_tree.append(Interval(4,8))
        interval_tree.append(Interval(12,17))

        interval_tree.dfs_inorder_iterative()

        interval = interval_tree.find_overlap(Interval(2,3))

        print(interval)


if __name__ == '__main__':
    TreeRunner.run()
    