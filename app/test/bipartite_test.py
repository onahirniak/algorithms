import unittest
from app.main.graphs.bipartite import Bipartite

class BipartiteTests(unittest.TestCase):

    def test_should_be_bipartite(self):
        sut = Bipartite()

        result = sut.is_biraptite(4, [[1,2],[1,3],[2,4]])

        self.assertTrue(result)

    def test_should_not_be_bipartite(self):
        sut = Bipartite()

        result = sut.is_biraptite(5, [[1,2],[2,3],[3,4],[4,5],[1,5]])

        self.assertFalse(result)