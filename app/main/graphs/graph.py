from collections import defaultdict
from heapq import *

class Graph(object):
    def __init__(self, g=None):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, distance=1):
        self.graph[u].append((v, distance));

    def bfs(self, start):
        visited = [False] * (len(self.graph)) 

        q = [start]
        visited[start] = True

        while q:
            vertex = q.pop(0)

            print(vertex, end = " ")

            for sibling, distance in self.graph[vertex]:
                if not visited[sibling]:
                    q.append(sibling)
                    visited[sibling] = True

    def dfs(self, start):
        visited = [False] * (len(self.graph))

        self.dfs_util(start, visited)
    
    def dfs_util(self, vertex, visited):
        visited[vertex] = True

        print(vertex, end = " ")

        for sibling, distance in self.graph[vertex]:
            if not visited[sibling]:
                self.dfs_util(sibling, visited)
    
    def shortest_path(self, start, end):
        q, seen, dist = [(0,start)], set(), {start: 0}

        while q:
            (cost,v1) = heappop(q)
            if v1 in seen: continue

            seen.add(v1)

            if v1 == end: return dist

            for v2, c in self.graph[v1]:
                if v2 in seen: continue

                total_cost = cost+c

                if v2 not in dist or total_cost < dist[v2][0]:
                    dist[v2] = (total_cost, v1)
                    heappush(q, (total_cost, v2))

        return dist
