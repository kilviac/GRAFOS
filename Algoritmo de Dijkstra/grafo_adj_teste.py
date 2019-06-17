from grafo_adj import *
import unittest

class TestGrafo(unittest.TestCase):
    def setUp(self):
        self.g1 = Grafo([], [])
        self.g2 = Grafo([], [])
        self.g3 = Grafo([], [])

        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG']:
            self.g1.adiciona_vertice(i)
        for i in ['A-B', 'A-L', 'A-M', 'B-L', 'B-C', 'L-O', 'M-S', 'M-P', 'N-M', 'P-N', 'C-O', 'O-N', 'O-R', 'N-R',
                  'O-Q', 'C-D', 'D-E', 'Q-T', 'R-S', 'R-U', 'S-V', 'V-W', 'T-G', 'E-F', 'U-G', 'U-F', 'U-AA', 'V-G',
                  'F-G', 'G-AA', 'AA-W', 'G-H', 'BB-G', 'W-X', 'AA-CC', 'CC-BB', 'X-Y', 'X-DD', 'DD-Z', 'CC-Y', 'CC-EE',
                  'H-I', 'H-FF', 'I-BB', 'I-J', 'J-GG', 'Z-J', 'J-K', 'GG-K']:
            self.g1.adiciona_aresta(i)

        for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            self.g2.adiciona_vertice(i)
        for i in ['A-B', 'A-C', 'B-D', 'D-C', 'D-H', 'H-F', 'C-E', 'F-E', 'E-G', 'D-F', 'G-F']:
            self.g2.adiciona_aresta(i)

        for i in ['A', 'B', 'C', 'D', 'E']:
            self.g3.adiciona_vertice(i)
        for i in ['A-B', 'A-E', 'B-E', 'E-B', 'B-C', 'E-C', 'E-D', 'D-C', 'C-D']:
            self.g3.adiciona_aresta(i)

    def teste_dijkstra(self):
        carga1 = ['D', 'G', 'X', 'Z']

        self.assertEqual(self.g1.dijkstra('A', 'K', 3, carga1), ['A-B', 'B-C', 'C-D', 'D-E', 'E-F', 'F-G', 'G-H', 'H-I', 'I-J', 'J-K'])
        self.assertEqual(self.g1.dijkstra('A', 'K', 5, carga1), ['A-M', 'M-S', 'S-V', 'V-G', 'G-H', 'H-I', 'I-J', 'J-K'])
        self.assertEqual(self.g2.dijkstra('B', 'G', 1, 'D'), ['B-D', 'D-C', 'C-E', 'E-G'])
        self.assertEqual(self.g3.dijkstra('A', 'D', 1, 'B'), ['A-B', 'B-C', 'C-D'])