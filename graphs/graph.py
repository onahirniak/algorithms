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
        q, seen, dist = [(0,start,())], set(), {start: 0}

        while q:
            (cost,v1,path) = heappop(q)
            if v1 in seen: continue

            seen.add(v1)
            path += (v1,)

            if v1 == end: return (cost, path)

            for v2, c in self.graph[v1]:
                if v2 in seen: continue

                # Not every edge will be calculated. The edge which can improve the value of node in heap will be useful.
                if v2 not in dist or cost+c < dist[v2]:
                    dist[v2] = cost+c
                    heappush(q, (cost+c, v2, path))

        return float("inf")
