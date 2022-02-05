# https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/

class Grafo(object):

    def __init__(self, n):  # inicializa as estruturas base do grafo

        self.matriz = []

    def inicializaMatriz(self, n):

        for i in range(n):
            self.matriz.append([0] * n)  # inicializa a matriz de valores com 0

    def atribuiPeso(self, linha, coluna, peso):  # atribui os pesos das arestas na matriz

        self.matriz[linha - 1][coluna - 1] = peso
        self.matriz[coluna - 1][linha - 1] = peso

    def ordem(self):  # ordem = nº de vértices = nº de colunas ou nº de linhas da matriz, já que ambos são iguais
        ordem = len(self.matriz)

        return ordem

    def tamanho(self):
        tamanho = 0

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if (self.matriz[i][j] != 0):
                    tamanho += 1
        # sabemos que a matriz contém o mesmo peso 2x, uma em cada linha dos vértices ligados, logo, 
        # basta dividir tamanho por 2, para obter a quantidade de arestas
        tamanho = (tamanho / 2)

        return int(tamanho)

    def retornaVizinhos(self, vertice):
        vizinhos = []
        for i in range(len(self.matriz)):
            if self.matriz[vertice-1][i] != 0:
                vizinhos.append(i+1)
        return vizinhos
            # execucao


    def grauVertice(self, vertice):
        grau = 0
        for i in range(len(self.matriz)):
            if self.matriz[vertice - 1][i] != 0:
                grau += 1
        return grau


# arquivo = open('C:\\Users\\victo\\Desktop\\Grafos-TPI\\src\\grafo.txt', 'r')
arquivo = open('grafo.txt', 'r')

n = int(arquivo.readline())

grafo = Grafo(n)

grafo.inicializaMatriz(n)

for linha in arquivo:  # implementar método leitura de arquivo
    linha = linha.split(' ')
    grafo.atribuiPeso((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))

arquivo.close()

print("Grafo: ", grafo.matriz)

print("Ordem do Grafo: ", grafo.ordem())

print("Tamanho do Grafo: ", grafo.tamanho())

vizinhos = grafo.retornaVizinhos(1)

print("Vizinhos Vertice 1", grafo.retornaVizinhos(1))

print("Vizinhos Vertice 2", grafo.retornaVizinhos(2))

print("Vizinhos Vertice 3", grafo.retornaVizinhos(3))

print("Vizinhos Vertice 3", grafo.retornaVizinhos(4))

print("Vizinhos Vertice 3", grafo.retornaVizinhos(5))

print("Grau Vertice 1: ", grafo.grauVertice(1))

print("Grau Vertice 2: ", grafo.grauVertice(2))

print("Grau Vertice 3: ", grafo.grauVertice(3))

print("Grau Vertice 4: ", grafo.grauVertice(4))

print("Grau Vertice 5: ", grafo.grauVertice(5))
