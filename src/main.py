
import grafo


mGrafo = grafo.Grafo()

def printMenu():
    print("_"* 60)
    print(3*"\t","MENU")
    print("_"* 60)

def inicializar(tipoEntrada):
    if tipoEntrada == 1:
        nomeArquivo = input("Digite o nome do arquivo Json: ")
        grafo.lerJson(nomeArquivo)
        nomeArquivo = nomeArquivo.replace("json","txt")
    else:
        nomeArquivo = input("Digite o nome do arquivo txt: ")
  
    arquivo = open(f'.\\src\\{nomeArquivo}', 'r')
    print("Grafo inicializado")
    n = int(arquivo.readline())
    

    mGrafo.inicializaMatriz(n)

    for linha in arquivo:  # implementar método leitura de arquivo
        linha = linha.split(' ')
        mGrafo.atribuiPeso((int(linha[0])), (int(linha[1])), (float(linha[2].replace('\n', ''))))
    arquivo.close()

    print("Grafo inicializado")
       
def escolherArquivo(mGrafo):
    print("_"* 60)
    print(3*"\t","MENU")
    print("_"* 60)
    print("Escolha o formato da entrada de arquivo:\n1) Json\n2) txt")
    tipo = int(input("->"))
    inicializar(tipo)

def menuFuncoes():
    while True:
        printMenu()
        print("1) Busca em Largura")
        print("2) Numero de componentes conexas do grafo e os vértices de cada componente")
        print("3) Verificar se possui ciclo")
        print("4) Densidade")
        print("5) Verificar se um vertice e articulacao")
        print("6) Verificar se um grafo é euleriano ")
        print("0) Sair")
        escolha = int(input("->"))

        if mGrafo == None: 
            print("Primeiro Inicialize o Grafo")
            break
           
        elif escolha == 1:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            mGrafo.buscaEmLargura(vertice)

        elif escolha == 2:
            mGrafo.componentesConexas()
                          
        elif escolha == 3:
            print("O Grafo possui ciclo") if mGrafo.verificaCiclo() else print("O Grafo nao possui ciclo")

        elif escolha == 4:
            print(F"A desidade do grafo e {mGrafo.densidade()}")
            
        elif escolha == 5:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            print("O vertice e articulacao") if mGrafo.articulacao(vertice) else print("O vertice nao e articulacao") 
                          
        elif escolha == 6:
            mGrafo.verificarEuliriano()
        else:
            break

      


    
    



while True:
    printMenu()
    print("1) Escolher o arquivo")
    print("2) Usar as funcoes do grafo")
    print("3) Converter o grafo para Json")
    print("4) Sair")
    escolha = int(input("->"))
    if escolha == 1:
        escolherArquivo(mGrafo)

    if escolha == 2:
        if mGrafo == None: 
            print("Primeiro Inicialize o Grafo")
        else:
            menuFuncoes()

    if escolha == 3:
        if mGrafo == None: 
            print("Primeiro Inicialize o Grafo")
        else:
            mGrafo.escreverJson()

    if escolha == 4:
            break
    
       
