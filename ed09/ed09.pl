conectado(1,2). 
conectado(3,4). 
conectado(5,6).
conectado(7,8). 
conectado(9,10). 
conectado(12,13).
conectado(13,14). 
conectado(15,16). 
conectado(17,18). 
conectado(19,20). 
conectado(4,1). 
conectado(6,3). 
conectado(4,7). 
conectado(6,11). 
conectado(14,9). 
conectado(11,15). 
conectado(16,12). 
conectado(14,17). 
conectado(16,19).

caminho(X,Y):-
    conectado(X,Y);
    conectado(X,Z),
    conectado(Z,Y).
caminho(X, Y):-
    conectado(X,Y);
    conectado(X,Z),
    conectado(Z,L),
    conectado(L,Y).

"caminho(13,X).
 X = 14
X = 9
X = 17
X = 14
X = 10
X = 18
caminho(5,10) false
caminho(1,X).
X = 2
X = 2"
 


    