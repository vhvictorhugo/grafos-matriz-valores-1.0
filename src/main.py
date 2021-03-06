
import grafo


mGrafo = grafo.Grafo()

def printMenu():
    print("_"* 60)
    print(3*"\t","MENU")
    print("_"* 60)

def inicializar(tipoEntrada):
    if tipoEntrada == 1:
        nomeArquivo = input("Digite o nome do arquivo Json: ")
        mGrafo.lerJson(nomeArquivo)
        nomeArquivo = nomeArquivo.replace("json","txt")
    else:
        nomeArquivo = input("Digite o nome do arquivo txt: ")
    try:
        arquivo = open(f'.\\src\\{nomeArquivo}', 'r')
    except:
        print("Erro ao abrir o arquivo")
        return False
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
        print("1) Ordem do grafo")
        print("2) Tamanho do grafo")
        print("3) Densidade")
        print("4) Vizinho de um vertice")
        print("5) Grau de um vertice")
        print("6) Verificar se um vertice e articulacao")
        print("7) Busca em Largura")
        print("8) Numero de componentes conexas do grafo e os vértices de cada componente")
        print("9) Verificar se possui ciclo")
        print("10) Verificar se um grafo é euleriano ")
        print("11) Distancia e caminho minimo ")
        print("12) A árvore geradora mínima de um grafo ")
        print("13) Mostrar a matriz do grafo")
        print("0) Sair")
        
        escolha = int(input("->"))

        if mGrafo == None: 
            print("Primeiro Inicialize o Grafo")
         
           
        elif escolha == 1:
            print("Ordem do grafo: ",mGrafo.ordem())
      

        elif escolha == 2:
            print("Tamanho do grafo: ",mGrafo.tamanho())
     
        elif escolha == 3:
            print("A desidade do grafo e ",mGrafo.densidade())
              
        elif escolha == 4:
            vertice = int(input("Escolha um verticer para saber seu vizinhos:\n->"))
            print("Vizinho de um vertice:",mGrafo.retornaVizinhos(vertice))
              
        elif escolha == 5:
            vertice = int(input("Escolha um vertice:\n->"))
            print("Vertice de grau:",mGrafo.grauVertice(vertice))
             
        elif escolha == 6:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            print("O vertice e articulacao") if mGrafo.articulacao(vertice) else print("O vertice nao e articulacao") 
                          
        elif escolha == 7:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            print("busca em largura:")
            mGrafo.buscaEmLargura(vertice)

        elif escolha == 8:
           printCompConex()

        elif escolha == 9:
            print("O Grafo possui ciclo") if mGrafo.verificaCiclo() else print("O Grafo nao possui ciclo")

        elif escolha == 10:
            mGrafo.verificarEuliriano()
        
        elif escolha == 11:
            vertice = int(input("Escolha um vertice pra comecar:\n->"))
            mGrafo.menorCaminhoVertice(vertice)
            
        elif escolha == 12:
            printArvoreMinima()
        
        elif escolha == 13:
            print("Matriz do grafo:")
            for linha in mGrafo.matriz:
                print(linha)
        else:
            break
def printArvoreMinima():
    n=mGrafo.ordem()
    cont=0
    for i in range(n):
        if mGrafo.componentesConexas(n)[1] == [i]*n:
            cont+=1
    if cont != 0:
        n=mGrafo.ordem()
        mst = mGrafo.primMST(n)
        # Criando e escrevendo em arquivos de texto (modo 'w'). escrita
        arquivo = open('arq01.txt','w')

        arquivo.write(str (n) + '\n')

        for i in range(1, n):
            aresta1, aresta2, peso = mGrafo.getParams(mst, i)
            arquivo.write(str (aresta1) + ' ' + str (aresta2) + ' ' + str (peso) + '\n')
        arquivo.close()
    else:
        print("Componete conexo, logo nao eh possivel!")
def printCompConex():
    n=mGrafo.ordem()
    print("Numero de componentes conexas: ", mGrafo.componentesConexas(n)[0])
    mGrafo.mostraVizinhosComponente(mGrafo.componentesConexas(n)[1])


while True:
    printMenu()
    print("1) Escolher o arquivo")
    print("2) Usar as funcoes do grafo")
    print("3) Converter o grafo para Json")
    print("0) Sair")
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
            

    if escolha == 0:
            break
    
       
