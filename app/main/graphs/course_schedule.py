import collections

'''
207. Course Schedule - https://leetcode.com/problems/course-schedule/
'''
class CourseSchedule():
    def can_finish(self, n, courses):
        if not courses: return True

        graph = collections.defaultdict(list)
        colored = [0] * n

        for u,v in courses:
            graph[u].append(v)

        for v in range(n):
            if not colored[v] and self.has_cycle(graph, v, colored):
                return False

        return True

    def has_cycle(self, graph, vertex, colored):
        colored[vertex] = 1

        for u in graph[vertex]:
            if colored[u] == 1:
                return True
            if not colored[u] and self.has_cycle(graph, u, colored):
                return True

        colored[vertex] = 2

        return False