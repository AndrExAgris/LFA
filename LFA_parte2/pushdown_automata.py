import random

from stack import stack
from states import Q0,Q1,Qf, Qs

def automata(fita):
    global stack
    initial_stack = stack.copy()
    print(initial_stack)
    Q0()
    a = True
    print(stack)
    while fita != []:
        result = Q1(fita)
        print(result)
        initial_stack = stack.copy()
        if result is None and initial_stack == []:
            Qf()
            break
        if not fita and result[0] == 'erro':
            Qs(result,pilha=initial_stack)
            break
    return 0


def add_erro(fita):
    
    indices_sem_erro = [i for i, char in enumerate(fita) if char in ('car_a', 'car_b', 'car_c', 'car_d', 'mod_aa', 'mod_ab', 'mod_ba', 'mod_bb', 'mod_ca', 'mod_cb', 'mod_da', 'mod_db', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2')]
       
    for i in range(indices_sem_erro[-1] + 1, len(fita)):
        if random.random() < 0.2:
            fita[i] = 'erro'
    
    return fita