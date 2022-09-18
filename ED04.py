from __future__ import annotations  
from dataclasses import dataclass
from typing import List
from typing import Callable


@dataclass
class Estado:
  nodo: List
  pai: Estado
  custo: float
  memoria: number

@dataclass
class Problema:
  estado_inicial: List
  acoes: List[str]
  funcao_sucessora: Callable[[List], List]
  funcao_objetivo: Callable[[List], bool]


  def solucao(estado: Estado) -> List[Estado]:
    lista = [estado]
    while estado.pai != None:
      estado = estado.pai
      lista.append(estado)

    lista.append(estado) 
    lista.reverse()
    
    return lista
from pprint import pprint

def busca(problema: Problema) -> List:
  
  """
    Implementação do algoritimo

    :param problema: definição

  
  """  
  # Inicialmente somente o estado inicial está na fronteira
  fronteira = [problema.estado_inicial]


  while True:

    pprint('Fronteira: ')
    pprint([e.nodo for e in fronteira])

    if not fronteira:
      raise RuntimeError('Nenhuma solução encontrada')
    # Remove o próximo elemento da fronteira
    estado = fronteira.pop(0) # FIFO - Busca em largura
    #nodo = fronteira.pop()  # LIFO - Busca em profundidade

    #fronteira.sort(key=lambda e: e.custo)
    #estado = fronteira.pop(0)   # Heap - Busca de custo uniforme  

    pprint('Estado visitado: ')
    pprint(estado.nodo)
    pprint(f'Custo do caminho: {estado.custo}')
    M = 0

    # Testa o objetivo
    if problema.funcao_objetivo(estado):
      M = 1
      return problema.solucao(estado)

    # Expande o estado atual e adiciona os vizinhos na fronteira
    fronteira += problema.funcao_sucessora(estado) 
#Modelagem do problema

def expansao(estado: Estado) -> List[Estado]:
  vizinhanca = []
  M = 0 
  def copia_todos():
    return A.copy(), B.copy(), C.copy()
    
  if problema.funcao_objetivo(estado):
      M = 1
      return problema.solucao(estado)

  A = estado.nodo[0]
  B = estado.nodo[1]
  C = estado.nodo[2]
  print(A)
  # [A -> B]
  if A and (not B or  A[-1] < B[-1]) and M == 0 :
    a,b,c = copia_todos()
    b.append(a.pop())
    vizinhanca.append(
        Estado(
        nodo = [a, b, c],
        pai = estado,
        custo = estado.custo + 1,
        memoria = M)
    )
  
  # [A -> C]
  if A and (not C or A[-1] < C[-1]) and M == 0 :
    a,b,c = copia_todos()
    c.append(a.pop())
    vizinhanca.append(
        Estado(
        nodo = [a, b, c],
        pai = estado,
        custo = estado.custo + 1,
        memoria = M)
    )

  # [B -> A]
  if B and (not A or  B[-1] < A[-1]) and M == 0:
    a,b,c = copia_todos()
    a.append(b.pop())
    vizinhanca.append(
        Estado(
        nodo = [a, b, c],
        pai = estado,
        custo = estado.custo + 1,
        memoria = M)
    )

  # [B -> C]
  if B and (not C or B[-1] < C[-1]) and M == 0:
    a,b,c = copia_todos()
    c.append(b.pop())
    vizinhanca.append(
        Estado(
        nodo = [a, b, c],
        pai = estado,
        custo = estado.custo + 1,
        memoria = M)
    )
  # [C -> A]
  if C and (not A or C[-1] < A[-1]) and  M == 0:
    a,b,c = copia_todos()
    a.append(c.pop())
    vizinhanca.append(
        Estado(
        nodo = [a, b, c],
        pai = estado,
        custo = estado.custo + 1,
        memoria = M)
    )
  
  # [C -> B]
  if C and (not B or C[-1] < B[-1]) and M == 0:
    a,b,c = copia_todos()
    b.append(c.pop())
    vizinhanca.append(
        Estado(
        nodo = [a, b, c],
        pai = estado,
        custo = estado.custo + 1,
        memoria = M)
    )

  return vizinhanca

def teste_objetivo(estado: Estado):
  if estado.nodo == [[], [], [3, 2, 1]]:
      return estado.nodo == [[], [], [3, 2, 1]]
      


problema = Problema(
    estado_inicial = Estado(
        nodo = [[3,2,1], [], []],
        pai = None,
        custo = 0,
        memoria = 0
    ),
    acoes=['A -> B',' A -> C','B -> A',' B -> C', 'C -> A','C -> B'],
    funcao_sucessora = expansao,
    funcao_objetivo =  teste_objetivo,
    
    )

solucao = busca(problema)