from .graph import Graph

class GraphRunner():
    @staticmethod
    def run():
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