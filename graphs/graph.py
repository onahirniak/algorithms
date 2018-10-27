from collections import defaultdict

class Graph(object):
    def __init__(self, g=None):
        self.graph = defaultdict(list) if not g else g
        
    def addEdge(self, u, v):
        self.graph[u].append(v);

    def bfs(self, start):
        visited = [False] * (len(self.graph)) 

        q = [start]
        visited[start] = True

        while q:
            vertex = q.pop(0)

            print(vertex, end = " ")

            for sibling in self.graph[vertex]:
                if not visited[sibling]:
                    q.append(sibling)
                    visited[sibling] = True

    def dfs(self, start):
        visited = [False] * (len(self.graph))

        self.dfs_util(start, visited)
    
    def dfs_util(self, vertex, visited):
        visited[vertex] = True

        print(vertex, end = " ")

        for sibling in self.graph[vertex]:
            if not visited[sibling]:
                self.dfs_util(sibling, visited)

    def find_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path

        if not self.graph[start]:
            return None
        
        for sibling in self.graph[start]:
            if sibling not in path:
                new_path = self.find_path(sibling, end, path)
                if new_path:
                    return new_path
        
        return None

    def find_all_paths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
            
        if not self.graph[start]:
            return []
        
        paths = []
        for sibling in self.graph[start]:
            if sibling not in path:
                new_paths = self.find_all_paths(sibling, end, path)
                for new_path in new_paths:
                    paths.append(new_path)
        
        return paths

    def find_shortest_path(self, start, end, path=[]):
        path = path + [start]

        if start == end:
            return path
        
        if not self.graph[start]:
            return None
        
        shortest = None

        for sibling in self.graph[start]:
            if sibling not in path:
                new_path = self.find_shortest_path(sibling, end, path)
                if not shortest or len(new_path) < len(shortest):
                    shortest = new_path

        return shortest