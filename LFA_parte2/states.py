from stack import populate
from helpers import separa_elementos
from transition import run_transitions


def Q0():
    global stack
    return populate(push_v="S")

def Q1(fita):
    global stack
    Q0()
    fita = separa_elementos(fita)
    fita = run_transitions(fita)  
            
    return fita

def Qf(fita):
    print("blablabla alguma coisa modelo do carro")
    return 0

def Qs(fita,pilha):
    print("Erro na fita, peça defeituosa")
    print(fita) 
    print(pilha)
    return 0







 