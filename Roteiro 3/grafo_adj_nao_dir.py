# -*- coding: utf-8 -*-
import random

class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class MatrizInvalidaException(Exception):
    pass


soma = 0
def tratar_grau(l, arestas, valor):
    if arestas[valor][l] != '-' and arestas[valor][l]>0:
        return 1
    elif valor==0: #esse valor eh o indice da aresta e nao pode ser negativo, limita o minimo que o indice valor pode assumir
        return 0
    else:
        return soma + tratar_grau(l, arestas, (valor - 1)) # funciona como um for so que o inverso, retornando a propria funçao

def percorrer_matriz(arestas):
    cont = 0
    for l in range(len(arestas)):
        for v in range(len(arestas)):
            if arestas[l][v] != '-' and arestas[l][v]!=0:
                cont = cont + 1
    if cont>0:
        return True
    else:
        return False



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

        if len(M) != len(N):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(N):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(N)):
            for j in range(len(N)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i>j and not(M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')


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

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA)+1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

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
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adiciona_vertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.vertice_valido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v) # Adiciona vértice na lista de vértices
            self.M.append([]) # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) -1:
                    self.M[k].append(0) # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-') # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adiciona_aresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.aresta_valida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.aresta_valida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] -= 1
            else:
                self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def caminho_eleriano(self):
        pass

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' '*(self.__maior_vertice)

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

    def caminho_euleriano(self):
        vertices = ver_aux = self.N
        arestas = self.M
        lista_grau = []
        cont = aux = 0

        for v in ver_aux:
            for i in vertices:
                if i == v:
                    a = vertices.index(i)
                    break

            for j in arestas[a]:
                if j != '-' and j > 0:
                    cont += j

            for k in arestas:
                c = arestas.index(k)
                if c != a:
                    if k[a] != '-' and k[a] > 0:
                        cont += k[a]

            lista_grau.append(cont)
            cont = 0

        for l in lista_grau:
            if l % 2 != 0:
                aux += 1

        if aux > 2:
            return False

        return True

    def vertices_adj(self):
        arestas = self.M
        vertice = self.N
        cont = 0
        cont2 = 0
        lAuxx = []

        for i in arestas:
            v = arestas[cont]
            for j in v:
                x = v[cont2]
                if v[cont2] > 0:
                    element = vertice[cont] + '-' + vertice[cont2]
                    lAuxx.append(element)

                cont2 = cont2 + 1
            cont = cont + 1
            cont2 = 0
        return lAuxx


    #def list_adj(self):

    def grau(self, v):
        posicao = self.N.index(v)
        cont = 0
        for i in range(len(self.M)):
            for a in range(len(self.M)):
                if (i == posicao or a == posicao) and self.M[i][a] != '-':
                    cont += self.M[i][a]
        return cont

    def caminho(self):
        arestas = self.M
        vertices = self.N
        flag = False
        List_rota = []



        if self.caminho_euleriano():
            for i in range(len(vertices)):
                if self.grau(vertices[i])%2 != 0:
                    vatual = vertices[i]
                    break
                x = random.choice(range(len(vertices))) #escolhe um vertice aleatorio se todos os graus forem par
                vatual = vertices[x]

            while percorrer_matriz(arestas): # roda ate que todos os elementos da matriz terem sido zerados
                for linha in range(len(arestas)):
                    for coluna in range(len(arestas)):
                        if vertices[linha] == vatual:
                            if (arestas[linha][coluna]!=0 and arestas[linha][coluna] != '-'):
                                if self.grau(vertices[coluna]) == 1:
                                    aux = tratar_grau(linha, arestas, len(arestas)-1) # confere se exsite alguma outra aresta que deve ser percorrida antes dessa de grau 1
                                    if aux>1:
                                        continue
                                List_rota.append(vertices[linha] + '-' + vertices[coluna])
                                vatual = vertices[coluna]
                                arestas[linha][coluna] = arestas[linha][coluna] - 1

                            elif coluna == len(arestas) - 1:   #caso nao tenha encontrado alguma aresta nas linhas, procura na coluna
                                for elemento in range(len(arestas)):
                                    if arestas[elemento][linha]!=0 and arestas[elemento][linha] != '-':
                                        if self.grau(vertices[elemento]) == 1:
                                            aux = tratar_grau(linha, arestas, len(arestas) - 1) #confere se existe alguma outra aresta que deve ser percorrida antes da de grau 1
                                            if aux > 1:  # se tiver, deve continuar percorrendo a matriz
                                                continue
                                        List_rota.append(vertices[linha] + '-' + vertices[elemento])
                                        vatual = vertices[elemento]
                                        arestas[elemento][linha] = arestas[elemento][linha] - 1
                                        break
            return List_rota