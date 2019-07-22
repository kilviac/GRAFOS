class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

    def arestaValida(self, aresta=''):
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

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str

    def vertices_nao_adjacentes(self):
        arestas = self.A.values()
        vertices = self.N
        list_aux = [] #lista de arestas
        list_nadj = [] #lista de vertices nao adjacentes
        list_adj = [] #lista de vertices adjacentes


        for i in vertices:
            for j in vertices:
                m = i + '-' + j #concatenando todas as combinaçoes possiveis de vertices
                list_aux.append(m) #adicionando todas as combinaçoes de vertices na lista auxiliar

        for f in list_aux:
            lo = f.split('-') #quebra as arestas onde tem o '-'
            aux = lo[0]
            lo[0] = lo[1]
            lo[1] = aux
            h = '-'.join(lo) #depois de alterar a posiçao dos vertices na ligaçao da aresta, ela vai ser novamente concatenada

            if f in arestas or h in arestas: #verifica se a combinaçao f dos vertices, ou o inverso esta dentro das arestas do grafo
                list_adj.append(f)
            else:
                list_nadj.append(f)

        return list_nadj


    def ha_laco(self):
        cont = 0
        arestas = self.A.values()
        l = []
        for i in arestas:
            l.append(i)

        for k in l:
            lo = k.split('-') #quebra as arestas, deixando apenas seus vertices

            if lo[0] == lo[1]:  #confere se os vertices que compoe as arestas sao iguais
                cont = cont + 1

        if cont>0: #se pelo menos houver uma aresta com vertices iguais, o contador ja vai ser maior que zero, mostrando que ha laço no grafo
            return True
        else:
            return False


    def grau(self, g):
        arestas = self.A.values()
        l = []
        cont = 0
        for i in arestas:
            l.append(i)

        for k in l:
            lo = k.split('-')  #quebra as arestas, deixando apenas seus vertices
            if lo[0] == g or lo[1] == g: #confere se um dos vertices que compoe a aresta e igual ao vertice que foi passaaado com parametro da funçao
                cont = cont + 1

        return cont  #retona a quantidade de vezes que o vertice apareceu, sendo o grau da funçao

    def ha_paralelas(self):
        arestas = self.A.values()
        l = []
        cont = 0

        for i in arestas:
            l.append(i)


        for m in arestas:
            lo = m.split('-') # quebra a string de vertices
            c = lo[0]
            lo[0] = lo[1]
            lo[1] = c

            h = '-'.join(lo) # lo eh uma variavel auxiliar pra trocar de posiçao os vertices que compoem a aresta, e o h vai juntar a combinaçao inversa
            for j in l:

                if m == j:  #confere se ha arestas iguais
                    cont = cont + 1
                if cont>1: #o contador tem que ser maior que 1, ja que uma aresta vai contar com ela mesma, e se achar outra que seja igual e que nao seja ela, siginifica que ha arestas paralelas
                    return True

            for f in l:
                lo = m.split('-') #quebra a aresta, deixando os vertices
                if lo[0] != lo[1]: #confere se os vertices nao sao iguais
                     if h == f:  #verifica se existe em l, uma aresta com os vertices invertidos
                        return True

            cont = 0

        return False


    def arestas_sobre_vertice(self, g):
        l = []

        for k,v in self.A.items():
            lo = v.split('-') # quebra o valor que esta no dicionario onde tem a barra que representa a ligaçao dos vertices
            if lo[0] == g or lo[1] == g: # serve para saber se um dos vertices que compoe a aresta e igual ao vertice passado como parametro da funçao
                l.append(k)  # coloca a chave que possui o vertice passado como parametro na lista de chaves
        return l  #retono de todas as arestas que possuem o vertice passado como parametro

    def eh_completo(self):
        arestas = self.A.values()
        vertices = self.N
        lis_aux = []

        for j in arestas:
            lis_aux.append(j)


        for i in vertices:
            for j in vertices:
                var_aux1 = i + '-' + j  # concatena todas as combinaçoes de vertices
                var_aux2 = j + '-' + i # concatena todas as combinaços de vertices alterando a posiçao dos vertices na composiçao da aresta

                if i != j:  # ja que laços nao influenciam nesse caso para saber se o grafo e completo

                    if not (var_aux1 in lis_aux or var_aux2 in lis_aux):  #confere se nenhuma das combinaçoes var_aux1 ou var_aux2 estao na lista de arestas, se nao tiveren retorna falso
                        return False


        return True