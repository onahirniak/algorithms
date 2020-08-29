import unittest
from app.main.graphs import Graph

class GraphTests(unittest.TestCase):

    def test_should_find_shortest_path(self):
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

        distances = g.shortest_path("A", "F")

        self.assertEqual(distances['F'], (11, 'D'))
        self.assertEqual(distances['D'], (5, 'A'))

    def test_should_not_find_shortest_path(self):
        g = Graph()

        g.add_edge("A", "B", 7)
        g.add_edge("A", "D", 5)
        g.add_edge("C", "D", 5)

        distances = g.shortest_path("A", "C")

        self.assertTrue('C' not in distances)


        