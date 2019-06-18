from grafo import *
import unittest

class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.g1 = Grafo()
        self.g2 = Grafo()
        self.g3 = Grafo()

        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
            self.g1.adicionaVertice(i)
        for i in ['A-B', 'A-E', 'B-F', 'C-G', 'D-E', 'D-H', 'E-H', 'F-G', 'F-I', 'F-J', 'G-J']:
            self.g1.adicionaAresta(i)

        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            self.g2.adicionaVertice(i)
        for i in ['A-B', 'A-C', 'B-D', 'B-E', 'C-F', 'C-G', 'G-H']:
            self.g2.adicionaAresta(i)

        for i in ['A', 'B', 'C', 'D', 'E', 'F']:
            self.g3.adicionaVertice(i)
        for i in ['A-B', 'A-C', 'B-D', 'B-E', 'C-F']:
            self.g3.adicionaAresta(i)

    def test_dfs(self):
        self.assertEqual(self.g1.dfs('A'), [['A', 'B', 'F', 'G', 'C', 'J', 'I', 'E', 'D', 'H'] ['G-C', 'J-F', 'G-C', 'I-F', 'F-B', 'B-A', 'H-D', 'H-D', 'E-A']])
        self.assertEqual(self.g2.dfs('A'), [['A', 'B', 'D', 'E', 'C', 'F', 'G', 'H'] ['D-B', 'E-B', 'B-A', 'F-C', 'H-G', 'G-C', 'C-A']])
        self.assertEqual(self.g3.dfs('A'), [['A', 'B', 'D', 'E', 'C', 'F'] ['D-B', 'E-B', 'B-A', 'F-C', 'C-A']])