# Branch and Bound

##### Grupo: Braian dos Santos Calot, João Victor Simões Gonçalves e Igor Fracalossi do Nascimento Lozorio.
 

## Explicação 
Esse programa foi feito utilizando o algoritmo A* como base.

Dada uma matriz onde 0 e -1 são células onde não é possível passar, e 1 ou maior indica uma célula onde é possivel passar
e o custo para passar por ela, o algoritmo encontra o melhor caminho entre uma célula inicial (START) e uma célula final (GOAL).
Neste caso, o caminho encontrado é o de menor custo.

## Exemplo
0	5	0	0	0
0	2	3	3	0
1	0	2	0	7
0	4	0	6	0
0	1	2	1	2
0	1	1	3	0

START: (0, 1)
GOAL: (5, 3)

Caminho encontrado:
(0, 1)  (1, 1)  (2, 0)  (3, 1)  (4, 2)  (5, 3)

Neste programa é possível utilizar as matrizes já definidas bastando escolher o START e GOAL para executar o algoritmo, ou se preferir,
é possível criar sua própria matriz para aplicar o algoritmo.
