from math import inf

const = 0
const1 = -1

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, N=[], M=[]):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''
        for v in N:
            if not(Grafo.vertice_valido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)
        self.N = N
        self.minE = None
        self.maxE = None
        self.arestas = {}
        self.contador = 1
        self.V = {}
        self.D = {}

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                aresta = N[i] + Grafo.SEPARADOR_ARESTA + N[j]
                if not(self.aresta_valida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = M

    def aresta_valida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existe_vertice(aresta[:i_traco])) or not(self.existe_vertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def vertice_valido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existe_vertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.vertice_valido(vertice) and self.N.count(vertice) > 0

    def primeiro_vertice_aresta(self, a: str):
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def segundo_vertice_aresta(self, a: str):
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def indice_primeiro_vertice_aresta(self, a: str):
        return self.N.index(self.primeiro_vertice_aresta(a))

    def indice_segundo_vertice_aresta(self, a: str):
        return self.N.index(self.segundo_vertice_aresta(a))

    def existe_aresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.aresta_valida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.indice_primeiro_vertice_aresta(a)][self.indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)
            self.M.append([])
            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0)
                self.M[self.N.index(v)].append(0)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        peso = a[-1]
        if self.aresta_valida(a[0]):
            self.M[self.indice_primeiro_vertice_aresta(a[0])][self.indice_segundo_vertice_aresta(a[0])] += 1
            aresta = "a{}".format(self.contador)
            self.contador += 1
            self.D[aresta] = [a[0], peso]
            self.arestas[aresta] = [a[0], peso]
            if self.minE is None:
                self.minE = aresta
            elif peso < self.D[self.minE][-1]:
                self.minE = aresta
            elif peso > self.D[self.maxE][-1]:
                self.maxE = aresta
            elif peso < self.arestas[self.minE][-1]:
                self.minE = aresta
            if self.maxE is None:
                self.maxE = aresta
            elif peso > self.arestas[self.maxE][-1]:
                self.maxE = aresta
            if a[0][0] in self.V.keys():
                if aresta not in self.V[a[0][0]]:
                    self.V[a[0][0]].append(aresta)
            else:
                self.V[a[0][0]] = [aresta]
            if a[0][-1] in self.V.keys():
                if aresta not in self.V[a[0][-1]]:
                    self.V[a[0][-1]].append(aresta)
            else:
                self.V[a[0][-1]] = [aresta]
        else:
            ArestaInvalidaException('A aresta ' + self.A[a[0]] + ' é inválida')

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str

    # PRIM

    def verticesAdjacentes(self, vertice, dictionary):
        vertices = self.V
        arestas = self.D
        lista = []

        for i in vertices[vertice]:
            for j in arestas[i][const]:
                if j != '-':
                    if j != vertice and j not in lista and j in dictionary.keys():
                        lista.append(j)
                        break
        return lista

    def menorAresta(self, vertice, inicio, dictAux):
        arestas = []
        aux = None

        for i in self.V[vertice]:
            if self.arestas[i][const] != self.arestas[i][const1]:
                if self.arestas[i][const] not in dictAux.keys() or self.arestas[i][const1] not in dictAux.keys():
                    arestas.append(i)
        for i in arestas:
            if vertice in self.arestas[i][const] and inicio in self.arestas[i][const]:
                if aux is None:
                    aux = i
                elif self.arestas[i][const1] < self.arestas[aux][const1]:
                    aux = i
        return aux

    def menorVertice(self):
        menorAresta = None

        for i in self.arestas.keys():
            if menorAresta is None:
                menorAresta = i
            elif self.arestas[i][const1] < self.arestas[menorAresta][const1]:
                menorAresta = i
        if menorAresta is not None:
            return self.arestas[menorAresta][const][const]

        return "Vazio"

    def Min(self, dictionary):
        aux = None

        try:
            inicio = min(dictionary.values())
        except:
            return "Vazio"

        if inicio != inf:
            for i in dictionary.keys():
                if dictionary[i] == inicio:
                    aux = i
        if aux is None:
            return 'Desconexo'

        return aux

    def Prim(self):
        vertices = self.N
        arestas = self.arestas
        vInicial = self.menorVertice()
        dict1 = {}
        dict2 = {}
        arvore = {}
        estado = True

        for i in vertices:
            dict2[i] = inf

        dict2[vInicial] = 0

        while True:
            if estado:
                inicio = vInicial
                estado = False
            else:
                inicio = self.Min(dict2)
            if inicio == "Desconexo":
                return False
            elif inicio == "Vazio":
                break
            else:
                dict2.pop(inicio)
                verticeAdj = self.verticesAdjacentes(inicio, dict2)
                for i in verticeAdj:
                    menorAresta = self.menorAresta(i, inicio, dict1)
                    dict2[i] = arestas[menorAresta][const1]
                    if i not in dict1.keys():
                        dict1[i] = menorAresta
                    else:
                        if arestas[menorAresta][const1] < arestas[dict1[i]][const1]:
                            dict1[i] = menorAresta

        for i in dict1.values():
            arvore[i] = self.arestas[i]

        return arvore

    # KRUSKAL

    def pilha(self, dictionary):
        lista = dictionary.values()
        buckets = {}
        listaOrdenada = {}

        for i in lista:
            if "bucket{}".format(const) not in buckets.keys():
                buckets["bucket{}".format(const)] = [i]
            else:
                buckets["bucket{}".format(const)].append(i)

        for aux in sorted(buckets.keys()):
            buckets[aux].sort(key = lambda a: a[const1])
            for i in buckets[aux]:
                for j in self.D.keys():
                    if self.D[j] == i:
                        listaOrdenada[j] = i

        return listaOrdenada

    def recursivaA(self, floresta, a, b):
        self.vertices = []
        self.estado = False
        self.recursivaB(floresta, a, b)
        return self.estado

    def recursivaB(self, floresta, a, b):
        if a == b:
            self.estado = True
        self.vertices.append(a)
        for i in floresta[a]:
            if i not in self.vertices:
                self.recursivaB(floresta, i, b)

    def Kruskal(self):
        pilha = self.pilha(self.D)
        floresta = {}
        arvore = {}
        vertices = []

        for i in self.N:
            floresta[i] = []

        if len(pilha) > 0:
            for i in pilha:
                a = pilha[i][const][const]
                b = pilha[i][const][const1]
                if not self.recursivaA(floresta, a, b):
                    floresta[a].append(b)
                    floresta[b].append(a)
                    arvore[i] = self.D[i]
                    if a not in vertices:
                        vertices.append(a)
                    elif b not in vertices:
                        vertices.append(b)

        return arvore