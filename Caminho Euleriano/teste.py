from grafo_adj_nao_dir import Grafo

g = Grafo([], [])

for i in ['M', 'T', 'B', 'R']:
    g.adiciona_vertice(i)
for i in ['M-T', 'M-T', 'M-B', 'M-B', 'M-R', 'M-R', 'B-R', 'T-R']:
    g.adiciona_aresta(i)
#print(g)


#print("M-T, T-R, R-M, M-B, B-R, R-M, M-B")

#print("\n")

g_c_e = Grafo([], [])
for i in ['A', 'B', 'C']:
    g_c_e.adiciona_vertice(i)
for i in ['A-B', 'B-C']:
    g_c_e.adiciona_aresta(i)

y = g.caminho()
print(y)