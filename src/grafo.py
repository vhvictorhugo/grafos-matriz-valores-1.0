# https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/

class Grafo(object):

    def __init__(self, n):  # inicializa as estruturas base do grafo
        
        self.matriz = []

    def inicializaMatriz(self, n):  

        for i in range (n):
            self.matriz.append([0]*n) # inicializa a matriz de valores com 0

    def atribuiPeso(self, linha, coluna, peso):

        self.matriz[linha][coluna] = peso
        self.matriz[coluna][linha] = peso

#     def get_vertices(self):
#         """ Retorna a lista de vértices do grafo. """
#         return list(self.adj.keys())


#     def get_arestas(self):
#         """ Retorna a lista de arestas do grafo. """
#         return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


#     def adiciona_arestas(self, arestas):
#         """ Adiciona arestas ao grafo. """
#         for u, v in arestas:
#             self.adiciona_arco(u, v)


#     def adiciona_arco(self, u, v):
#         """ Adiciona uma ligação (arco) entre os nodos 'u' e 'v'. """
#         self.adj[u].add(v)
#         # Se o grafo é não-direcionado, precisamos adicionar arcos nos dois sentidos.
#         self.adj[v].add(u)


#     def existe_aresta(self, u, v):
#         """ Existe uma aresta entre os vértices 'u' e 'v'? """
#         return u in self.adj and v in self.adj[u]


#     def __len__(self):
#         return len(self.adj)


#     def __str__(self):
#         return '{}({})'.format(self.__class__.__name__, dict(self.adj))


#     def __getitem__(self, v):
#         return self.adj[v]


# # Cria a lista de arestas.
# arestas = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('C', 'B'), ('C', 'E'), ('D', 'A'), ('E', 'B')]

# # Cria e imprime o grafo.
# grafo = Grafo(arestas)
# print(grafo.adj)

# print(grafo.get_vertices())

# print(grafo.get_arestas())

# print(grafo.existe_aresta('A', 'B'), grafo.existe_aresta('E', 'C'))

grafo = Grafo(5)

grafo.inicializaMatriz(5)

print(grafo.matriz)

grafo.atribuiPeso(1, 2, 1.2)

print(grafo.matriz)