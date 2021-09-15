
# <b>Branch and Bound</b>

## <b>Grupo:</b> Braian dos Santos Calot, João Victor Simões Gonçalves e Igor Fracalossi do Nascimento Lozorio.</br> 

## <b>Explicação</b>
<h3> 
    Esse programa foi feito utilizando o algoritmo <b>A*</b> como base. Dada uma matriz onde <b>0</b> e <b>-1</b> são células onde <b>não</b> é possível passar, e <b>1</b> ou <b>acima</b> indica uma célula onde é possível passar e o custo para passar por ela. O algoritmo encontra o melhor caminho entre uma célula inicial <b>( START )</b> e uma célula final <b>( GOAL )</b>. Neste caso, o caminho encontrado é o de <b>menor custo</b>.
</h3></br>

## <b>Exemplo</b>
<h3>
    0 &nbsp 5 &nbsp 0 &nbsp 0 &nbsp 0 </br> 
    0 &nbsp 2 &nbsp 3 &nbsp 3 &nbsp 0 </br>
    1 &nbsp 0 &nbsp 2 &nbsp 0 &nbsp 7 </br>
    0 &nbsp 4 &nbsp 0 &nbsp 6 &nbsp 0 </br>
    0 &nbsp 1 &nbsp 2 &nbsp 1 &nbsp 2 </br>
    0 &nbsp 1 &nbsp 1 &nbsp 3 &nbsp 0 </br>
</h3></br>

<h3>
    <b> START:</b> &nbsp ( 0, 1 ) </br>
    <b> GOAL: </b> &nbsp&nbsp ( 5, 3 )
</h3>

</br>

## <b>Caminho encontrado:</b></br>
<h3>
    ( 0 , 1 ) &nbsp ( 1 , 1 ) &nbsp ( 2 , 0 ) &nbsp ( 3 , 1 ) &nbsp ( 4 , 2 ) &nbsp ( 5 , 3 )
</h3></br>

<h3> 
    Neste programa é possível utilizar as matrizes já definidas bastando escolher o <b>START</b> e <b>GOAL</b> para executar o algoritmo, ou se preferir, é possível criar sua própria matriz para aplicar o algoritmo. 
</h3>

