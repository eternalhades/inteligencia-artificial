% questao_1
conta_elementos(_,[], 0).

conta_elementos(V,[H|T],N):-
    conta_elementos(V,T,NN),
    V = H,
    N is NN + 1,
    !.

conta_elementos(V,[_|T],N):-
    conta_elementos(V,T,N).

elem_repetidos([],[]).

elem_repetidos([H|T],[H|Z]):-
    conta_elementos(H,T,R),
    R > 0,
    conta_elementos(H,T,R2),
    R2 = 1,
    elem_repetidos(T,Z),
    !.

elem_repetidos([_|T],Z):-
    elem_repetidos(T,Z).

% questao_2
% Verifica que a lista da esquerda acabou
intercala_a_esquerda([],L2,LR):-
    intercalada([],L2, LR).

% Adiciona a cabeca da primeira lista (lista a esquerda) e chama predicado para intercalar o prox elemento da lista da direita
intercala_a_esquerda([H|T],L2,[H|TR]):-
    intercala_a_direita(T,L2,TR).

% Verifica que a lista da direita acabou
intercala_a_direita(L1,[],LR):-
	intercalada(L1,[],LR).

% Adiciona a cabeca da segunda lista (lista a direita) e chama predicado para intercalar o prox elemento da lista da esquerda
intercala_a_direita(L1,[H2|T2],[H2|TR]):-
    intercala_a_esquerda(L1,T2,TR).

% condicao de parada
intercalada([],[],[]).

% quando a primeira lista esta vazia, termina de adicionar os elementos da segunda
intercalada([],[H2|T2],[H2|TR]):-
    intercalada([],T2,TR).

% quando a segunda lista esta vazia, termina de adicionar os elementos da primeira
intercalada([H1|T1],[],[H1|TR]):-
    intercalada(T1,[],TR),
    !.

% lista nao vazia
intercalada(L1,L2,LR):-
    intercala_a_esquerda(L1,L2,LR),
    !.


% questao_3

e_lista([]).
e_lista([_|_]).
    
existe_menor(N,[H|_]):-
    N > H.

insercao_ord(N,[],[N|[]]):-
    not(e_lista(N)),
    !.

insercao_ord(_,[],[]).

insercao_ord([],[H1|T1],[H1|TR]):-
    insercao_ord([],T1,TR).

insercao_ord(N,[H1|T1],[N,H1|TR]):-
    N < H1,
    not(existe_menor(N,T1)),
    insercao_ord([],T1,TR),
    !.

insercao_ord(N,[H1|T1],[H1|TR]):-
    insercao_ord(N,T1,TR).
    
    % questao_4
adiciona_elementos_na_lista([],[]).

adiciona_elementos_na_lista([H1|T1],[H1|T2]):-
    adiciona_elementos_na_lista(T1,T2).
    
ordenada([],[]).

ordenada([H1|T1],L2):-
    insercao_ord(H1,L2,LR),
    ordenada(T1,LR).