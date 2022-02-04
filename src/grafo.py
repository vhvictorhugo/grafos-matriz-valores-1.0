# https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/

class Grafo(object):

    def __init__(self, n):  # inicializa as estruturas base do grafo
        
        self.matriz = []

    def inicializaMatriz(self, n):  

        for i in range (n):
            self.matriz.append([0]*n) # inicializa a matriz de valores com 0

    def atribuiPeso(self, linha, coluna, peso): # atribui os pesos das arestas na matriz

        self.matriz[linha-1][coluna-1] = peso
        self.matriz[coluna-1][linha-1] = peso

    def ordem(self):    # ordem = nº de vértices = nº de colunas ou nº de linhas da matriz, já que ambos são iguais
        ordem = len(self.matriz)

        return ordem
    
    def tamanho(self):
        tamanho = 0

        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if(self.matriz[i][j] != 0):
                    tamanho += 1

        # sabemos que a matriz contém o mesmo peso 2x, uma em cada linha dos vértices ligados, logo, 
        # basta dividir tamanho por 2, para obter a quantidade de arestas
        tamanho = (tamanho/2)

        return int (tamanho)

# execucao
arquivo = open('C:\\Users\\victo\\Desktop\\Grafos-TPI\\src\\grafo.txt', 'r')

n = int (arquivo.readline())

grafo = Grafo(n)

grafo.inicializaMatriz(n)

for linha in arquivo:   # implementar método leitura de arquivo
    linha = linha.split(' ')
    grafo.atribuiPeso((int (linha[0])), (int (linha[1])), (float (linha[2].replace('\n', ''))))

arquivo.close()

print("Grafo: ", grafo.matriz)

print("Ordem do Grafo: ", grafo.ordem())

print("Tamanho do Grafo: ", grafo.tamanho())