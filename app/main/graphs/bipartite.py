import collections

'''
886. Possible Bipartition - https://leetcode.com/problems/possible-bipartition/
'''
class Bipartite():
    def is_biraptite(self, n, dislikes):
        colors = [2] * (n + 1)

        graph = collections.defaultdict(list)

        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)

        for v in range(1, n):
            if colors[u] == 2 and not self.dfs(graph, v, colors, 0):
                return False
        
        return True
    
    def dfs(self, graph, vertex, colors, current_color):
        colors[vertex] = current_color

        for u in graph[vertex]:
            if colors[vertex] == colors[u]:
                return False
            if colors[u] == 2 and not self.dfs(graph, u, colors, not current_color):
                return False
        
        return True
