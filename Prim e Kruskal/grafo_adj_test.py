from grafo_adj import *

grafo1 = Grafo([], [])
grafo2 = Grafo([], [])
grafo3 = Grafo([], [])

for i in ['J', 'C', 'E', 'P', 'M', 'T', 'Z']:
    grafo1.adiciona_vertice(i)
for i in [('C-J', 3), ('C-E', 1), ('C-P', 5), ('C-M', 4), ('C-T', 2), ('M-T', 3), ('M-P', 1), ('T-Z', 6), ('M-Z', 9)]:
    grafo1.adiciona_aresta(*i)

for i in ['A', 'B', 'C', 'D', 'E']:
    grafo2.adiciona_vertice(i)
for i in [('A-B', 2), ('A-D', 2), ('B-C', 6), ('C-D', 4), ('C-E', 3), ('D-E', 5)]:
    grafo2.adiciona_aresta(*i)

print(grafo1.prim())
print(grafo1.kruskal())