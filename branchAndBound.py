class No:
    def __init__(self, posicao, pai):
        self.posicao = posicao
        self.pai = pai
        self.g = 0
        self.h = 0
        self.f = 0
    
def getF(no):
    return no.f

def bnb(mat, start, goal):
    numCol = len(mat[0])
    numLin = len(mat)
    listaAberta = []
    listaFechada = []

    noStart = No(start, None)
    noGoal = No(goal, None)

    listaAberta.append(noStart)

    while(len(listaAberta)) > 0:
        
        listaAberta.sort(key=getF)

        noAtual = listaAberta.pop(0)

        listaFechada.append(noAtual)

        if(noAtual.posicao == noGoal.posicao):
            caminho = []
            while(noAtual.posicao != noStart.posicao):
                caminho.append(noAtual.posicao)
                noAtual = noAtual.pai
            caminho.append(noStart.posicao)
            return caminho
        
        x = noAtual.posicao[0]
        y = noAtual.posicao[1]

        proximos = [(x, y+1), (x+1, y+1), (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1), (x-1, y), (x-1, y+1)]

        for proximo in proximos:
            if(proximo[0] < 0 or proximo[1] < 0):
               continue

            if(proximo[0] >= numLin or proximo[1] >= numCol):
                continue

            if(mat[proximo[0]][proximo[1]] < 1):
                continue

            noProximo = No(proximo, noAtual)

            if(noProximo in listaFechada):
                continue 

            noProximo.g = calcularDistancia(noProximo, noStart)
            noProximo.h = calcularDistancia(noProximo, noGoal)
            noProximo.f = noProximo.g + noProximo.h + mat[proximo[0]][proximo[1]] + noProximo.pai.f

            if(addListaAberta(listaAberta, noProximo) == True):
                listaAberta.append(noProximo)

    return None

def calcularDistancia(noOrigem, noDestino):
    distX = abs(noOrigem.posicao[0] - noDestino.posicao[0])
    distY = abs(noOrigem.posicao[1] - noDestino.posicao[1])

    if(distX >= distY):
        return distX
    else:
        return distY

def addListaAberta(listaAberta, noProximo):
    for no in listaAberta:
        if(noProximo.posicao == no.posicao and noProximo.f >= noProximo.f):
            return False
    return True

mat1 = [[1, 0], 
        [0, 1]]

mat2 = [[1, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 1],
        [1, 0, 0, 0],
        [1, 1, 1, 0]] 

mat3 = [[1, 1, 1],
        [0, 0, 1],
        [0, 0, 1]]

mat4 = [[0, 1, 0, 0, 0],
        [0, 1, -1, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [0, -1, -1, 1, 0]]
        
mat5 =  [[0, 5, 0, 0, 0],
         [0, 2, 3, 3, 0],
         [1, 0, 2, 0, 7],
         [0, 4, 0, 6, 0],
         [0, 1, 2, 1, 2],
         [0, 1, 1, 3, 0]]

mat6 =  [[1, 0, 1],
         [0, 4, 0],
         [2, 0, 2],
         [0, 3, 0]]

mat7 =  [[1, 0, 0, 1, 0, 1],
         [1, 1, 0, 0, 0, 0],
         [1, 0, 1, 1, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [0, 0, 1, 0, 0, 1],
         [1, 1, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, 1],
         [0, 1, 0, 0, 1, 1],
         [1, 0, 0, 0, 1, 1]]      

mat8 =  [[1, 0, 0, 4, 0, 1],
         [2, 3, 0, 0, 0, 0],
         [8, 0, 2, 1, 2, -1],
         [0, 6, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, -1],
         [1, 2, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, -1],
         [0, 1, 0, 0, 1, 1],
         [5, 0, 0, 0, 1, -1]]

mat9 = [[0, 1, 0],
        [1, 0, 1],
        [10, 0, 12],
        [10, 0, 1],
        [0, 1, 0]]         

def imprimirMatriz(mat):
    lin = len(mat)
    col = len(mat[0])

    for linha in mat:
        for num in linha:
            print(f'{num:>3}', end=" ")
        print()

def verificarEntradas(mat, start, goal):
    lin = len(mat)
    col = len(mat[0])

    if((start[0] < 0 or start[1] < 0) or (goal[0] < 0 or goal[1] < 0)):
        return False

    if((start[0] >= lin or start[1] >= col) or (goal[0] >= lin or goal[1] >= col)):
        return False

    if(mat[start[0]][start[1]] == 0 or mat[start[0]][start[1]] == 0):
        return False

    return True

op = None
while op != 0:
    
    print("\n-----===Menu===-----")
    print("1. Matrizes Exemplo")
    print("2. Criar Matriz")
    print("0. Sair")
    print("--------------------")
    op = int(input("Digite a opção: "))

    if op == 1:        
        print("\nMatriz 1:\n")
        imprimirMatriz(mat1)
        print("\nMatriz 2:\n")
        imprimirMatriz(mat2)
        print("\nMatriz 3:\n")
        imprimirMatriz(mat3)
        print("\nMatriz 4:\n")
        imprimirMatriz(mat4)
        print("\nMatriz 5:\n")
        imprimirMatriz(mat5)
        print("\nMatriz 6:\n")
        imprimirMatriz(mat6)
        print("\nMatriz 7:\n")
        imprimirMatriz(mat7)
        print("\nMatriz 8:\n")
        imprimirMatriz(mat8)

        op2 = int(input("\nDigite o número da matriz que deseja trabalhar: "))
        print("Digite as coordenadas do START e GOAL, lembre-se: Só é possível começar e terminar em uma célula cujo o valor é igual ou maior que 1")
        startX = int(input("\nDigite a linha do START: "))
        startY = int(input("Digite a coluna do START: "))
        goalX = int(input("Digite a linha do GOAL: "))
        goalY = int(input("Digite a coluna do GOAL: "))
        
        start = (startX, startY)
        goal = (goalX, goalY)   

        if op2 == 1:
            if(verificarEntradas(mat1, start, goal)):
                path = bnb(mat1, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")  

        elif op2 == 2:
            if(verificarEntradas(mat2, start, goal)):
                path = bnb(mat2, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")

        elif op2 == 3:
            if(verificarEntradas(mat3, start, goal)):
                path = bnb(mat3, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")  

        elif op2 == 4:
            if(verificarEntradas(mat4, start, goal)):
                path = bnb(mat4, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")

        elif op2 == 5:
            if(verificarEntradas(mat5, start, goal)):
                path = bnb(mat5, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")

        elif op2 == 6:
            if(verificarEntradas(mat6, start, goal)):
                path = bnb(mat6, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")

        elif op2 == 7:
            if(verificarEntradas(mat7, start, goal)):
                path = bnb(mat7, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")

        elif op2 == 8:
            if(verificarEntradas(mat8, start, goal)):
                path = bnb(mat8, start, goal)
                print("\nMelhor caminho encontrado: \n")
                for i in range(len(path)-1, -1, -1):
                    print(path[i], end='\t')

                print()
            else:
                print("Informações inválidas! Tente novamente.")

        else:
            print("Informações inválidas! Tente novamente.")
    
    if op == 2:
        qtLin = int(input("Digite a quantidade de linhas: "))
        qtCol = int(input("Digite a quantidade de colunas: "))  
        print("\nPreencha a matriz: (Lembre-se: 0 ou -1 = não da pra passar por essa célula, 1 ou maior = é possível passar e o custo para passar por essa célula\n")
      
        matCriada = []
        for i in range(qtLin):
            linha = []
            for j in range(qtCol):
                num = int(input("Digite o elemento[" + str(i) + "][" + str(j) + "]: "))
                linha.append(num)
            matCriada.append(linha)

        print("\nMatriz criada:\n ")
        imprimirMatriz(matCriada)  

        print("\nDigite as coordenadas do START e GOAL, lembre-se: Só é possível começar e terminar em uma célula cujo o valor é igual ou maior que 1")
        startX = int(input("\nDigite a linha do START: "))
        startY = int(input("Digite a coluna do START: "))
        goalX = int(input("Digite a linha do GOAL: "))
        goalY = int(input("Digite a coluna do GOAL: "))
        
        start = (startX, startY)
        goal = (goalX, goalY)

        if(verificarEntradas(matCriada, start, goal)):
            path = bnb(matCriada, start, goal)
            print("\nMelhor caminho encontrado: \n")
            for i in range(len(path)-1, -1, -1):
                print(path[i], end='\t')

            print()
        else:
            print("Informações inválidas! Tente novamente.")

    elif op == 2:
        print("Opção 2")     
    
    elif op == 0:
       print("Saindo...") 
    else:
        print("Opção inválida! Tente novamente.")       
   