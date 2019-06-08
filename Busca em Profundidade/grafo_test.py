from grafo import *

g1 = Grafo()
g2 = Grafo()
g3 = Grafo()

# Grafo 1 - arestas de retorno: [D-B, E-B, B-A, F-C, H-G, G-C, C-A]
for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
    g1.adicionaVertice(i)
for i in ['A-B', 'A-C', 'B-D', 'B-E', 'C-F', 'C-G', 'G-H']:
    g1.adicionaAresta(i)

# Grafo 2
for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
    g2.adicionaVertice(i)
for i in ['A-B', 'A-E', 'B-F', 'C-G', 'D-E', 'D-H', 'E-H', 'F-G', 'F-I', 'F-J', 'G-J']:
    g2.adicionaAresta(i)

# Grafo 3 - arestas de retorno: [D-B, E-B, B-A, F-C, C-A]
for i in ['A', 'B', 'C', 'D', 'E', 'F']:
    g3.adicionaVertice(i)
for i in ['A-B', 'A-C', 'B-D', 'B-E', 'C-F']:
    g3.adicionaAresta(i)

g1.dfs('A')
print()
g2.dfs('A')
print()
g3.dfs('A')


#Grafo 1     #Grafo 2     #Grafo 3
# A          #A           #A
# B          #B           #B
# D          #F           #D
# E          #G           #E
# C          #C           #C
# F          #J           #F
# G          #I
# H          #E
             #D
             #H