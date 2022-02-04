# https://algoritmosempython.com.br/cursos/algoritmos-python/algoritmos-grafos/representacao-grafos/

class Grafo(object):

    def __init__(self, n):  # inicializa as estruturas base do grafo
        
        self.matriz = []

    def inicializaMatriz(self, n):  

        for i in range (n):
            self.matriz.append([0]*n) # inicializa a matriz de valores com 0

    def atribuiPeso(self, linha, coluna, peso):

        self.matriz[linha-1][coluna-1] = peso
        self.matriz[coluna-1][linha-1] = peso


# execucao
arquivo = open('C:\\Users\\victo\\Desktop\\Grafos-TPI\\src\\grafo.txt', 'r')

n = int (arquivo.readline())

print (n, type(n))

grafo = Grafo(n)

grafo.inicializaMatriz(n)

for linha in arquivo:
    linha = linha.split(' ')
    grafo.atribuiPeso((int (linha[0])), (int (linha[1])), (float (linha[2].replace('\n', ''))))

arquivo.close()

print(grafo.matriz)