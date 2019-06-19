import unittest
from grafo_adj import *


class TestGrafo(unittest.TestCase):

    def setUp(self):
        self.g_p = Grafo([], [])
        for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
            self.g_p.adiciona_vertice(i)
        for i in [['J-C', 3], ['C-E', 7], ['C-E', 2], ['C-P', 6], ['C-P', 2], ['C-M', 5], ['C-T', 9], ['M-T', 7], ['T-Z', 4]]:
            self.g_p.adiciona_aresta(i)

        self.g_c = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_c.adiciona_vertice(i)
        for i in [['J-C', 5], ['J-E', 10], ['J-P', 8], ['C-J', 9], ['C-E', 7], ['C-P', 1], ['E-J', 7], ['E-C', 4],
                  ['E-P', 6], ['P-J', 3], ['P-C', 9], ['P-E', 2]]:
            self.g_c.adiciona_aresta(i)

        self.g_l5 = Grafo([], [])
        for i in ['C', 'D']:
            self.g_l5.adiciona_vertice(i)
        for i in [['D-C', 5], ['C-C', 1]]:
            self.g_l5.adiciona_aresta(i)

        self.g_l6 = Grafo([], [])
        for i in ['J', 'C', 'E', 'P']:
            self.g_l6.adiciona_vertice(i)
        for i in [['J-C', 5], ['J-E', 10], ['J-P', 8], ['C-J', 9], ['C-E', 7], ['C-P', 1], ['E-J', 7], ['E-C', 4], ['E-P', 6], ['P-J', 3], ['P-C', 9], ['P-E',2]]:
            self.g_l6.adiciona_aresta(i)


    def test_Prim(self):
        self.assertEqual(self.g_p.Prim(), {'a1': ['J-C', 3],'a3': ['C-E', 2], 'a5': ['C-P', 2],'a6': ['C-M', 5],
                                           'a8': ['M-T', 7],'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c.Prim(), {'a10': ['P-J', 3], 'a12': ['P-E', 2], 'a6': ['C-P', 1]})
        self.assertEqual(self.g_l5.Prim(), {"a1": ['D-C', 5]})
        self.assertEqual(self.g_l6.Prim(), {'a6': ['C-P', 1], 'a12': ['P-E', 2], 'a10':['P-J',3]})

    def teste_Kruskal(self):
        self.assertEqual(self.g_p.Kruskal(), {'a1': ['J-C', 3], 'a3': ['C-E', 2], 'a5': ['C-P', 2], 'a6': ['C-M', 5],
                                              'a8': ['M-T', 7], 'a9': ['T-Z', 4]})
        self.assertEqual(self.g_c.Kruskal(), {'a10': ['P-J', 3], 'a12': ['P-E', 2], 'a6': ['C-P', 1]})
        self.assertEqual(self.g_l5.Kruskal(), {"a1": ['D-C', 5]})
        self.assertEqual(self.g_l6.Kruskal(), {'a6': ['C-P', 1], 'a12': ['P-E', 2], 'a10': ['P-J', 3]})