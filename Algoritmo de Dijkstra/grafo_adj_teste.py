from grafo_adj import *

vertices1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG']

arestas1 = ['A-B', 'A-L', 'A-M', 'B-L', 'B-C', 'L-O', 'M-S', 'M-P', 'N-M', 'P-N', 'C-O', 'O-N', 'O-R', 'N-R',
            'O-Q', 'C-D', 'D-E', 'Q-T', 'R-S', 'R-U', 'S-V', 'V-W', 'T-G', 'E-F', 'U-G', 'U-F', 'U-AA', 'V-G',
            'F-G', 'G-AA', 'AA-W', 'G-H', 'BB-G', 'W-X', 'AA-CC', 'CC-BB', 'X-Y', 'X-DD', 'DD-Z', 'CC-Y', 'CC-EE',
            'H-I', 'H-FF', 'I-BB', 'I-J', 'J-GG', 'Z-J', 'J-K', 'GG-K']

cargas1 = ['D', 'G', 'X', 'Z']

g1 = Grafo([], [])
for i in vertices1:
    g1.adiciona_vertice(i)
for i in arestas1:
    g1.adiciona_aresta(i)

vertices2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
arestas2 = ['A-B', 'A-C', 'B-D', 'D-C', 'D-H', 'H-F', 'C-E', 'F-E', 'E-G', 'D-F', 'G-F']
cargas2 = ['D']

g2 = Grafo([], [])
for i in vertices2:
    g2.adiciona_vertice(i)
for i in arestas2:
    g2.adiciona_aresta(i)

print(g1.dijkstra('A', 'K', 3, cargas1))
print(g2.dijkstra('B', 'G', 1, cargas2))