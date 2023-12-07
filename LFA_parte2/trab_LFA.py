import random


Symbols = ['a', 'b', 'c', 'd', 'a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2', 'r1', 'r2', 'm1', 'm2', 'v', 'f', 'x', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']

def separa_elementos(fita, Symbols=Symbols):
    elementos = []
    while len(fita) > 0:
        elemento = fita[0]
        elementos.append(elemento)
        fita = fita[1:]
        new_elementos = arruma_symbols(elementos, Symbols)
    return new_elementos



def arruma_symbols(elementos, Symbols=Symbols):
    new_elementos = []
    jit = False

    for x in range(len(elementos)):
        if jit:
            jit = False
            continue

        if x + 1 >= len(elementos):
            new_elementos.append(elementos[x])
            return new_elementos

        a = elementos[x] + elementos[x+1]
        if a in Symbols:
            new_elementos.append(a)
            jit = True
        else:
            new_elementos.append(elementos[x])

    return new_elementos

global stack
stack = []
def populate(pop_v="e", push_v="e"):
    Symbols = ['a', 'b', 'c', 'd', 'a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2', 'r1', 'r2', 'm1', 'm2', 'v', 'f', 'x', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']

   
    if pop_v != "e":
        pop_v = separa_elementos(pop_v, Symbols)
        for x in pop_v:
            while stack and stack[-1] == x:
                stack.pop()


    if push_v != "e":
        push_v = separa_elementos(push_v, Symbols)
        stack.extend(reversed(push_v))

    return None

def reset_stack():
    global stack
    stack.clear()


def reset_global_variables():
    global stack
    reset_stack() 

def epsilon_transition():
    global stack
    transitions = [
        ['S', 'aA'],
        ['A', 'a1A1'],
        ['A1', 'r1m1'],
        ['A', 'a2A2'],
        ['A2', 'r2m2vf'],
        ['S', 'bB'],
        ['B', 'b1B1'],
        ['B1', 'r1m1v'],
        ['B', 'b2B2'],
        ['B2', 'r2m2vf'],
        ['S', 'cC'],
        ['C', 'c1C1'],
        ['C1', 'r2m1'],
        ['C', 'c2C2'],
        ['C2', 'r2m2vf'],
        ['S', 'dD'],
        ['D', 'd1D1'],
        ['D1', 'r1m1vf'],
        ['D', 'd2D2'],
        ['D2', 'r2m2vf'],
    ]
    possible_transitions = [transition for transition in transitions if transition[0] == stack[-1]]

    if possible_transitions:
        random_transition = random.choice(possible_transitions)
        populate(pop_v=random_transition[0], push_v=random_transition[1])
        return 1
    return 0

def tape_transition(fita):
    global stack
    transitions = [
        ('a', 'e'),
        ('b', 'e'),
        ('c', 'e'),
        ('d', 'e'),
        ('a1', 'e'),
        ('a2', 'e'),
        ('b1', 'e'),
        ('b2', 'e'),
        ('c1', 'e'),
        ('c2', 'e'),
        ('d1', 'e'),
        ('d2', 'e'),
        ('r1', 'e'),
        ('r2', 'e'),
        ('m1', 'e'),
        ('m2', 'e'),
        ('v', 'e'),
        ('f', 'e'),
    ]

    for pop, push in transitions:
        if fita and stack and fita[0] == pop and stack[-1] == pop:
            if fita[0] == 'x':
                break
            populate(pop_v=pop, push_v=push)
            fita.pop(0)
            return 1
    
    if not stack:
        return 2

    return 0

def run_transitions(fita):
    global stack
    defect = random.randint(1, 99)
    if defect < 3:
        fita.append('x')
    
    while fita:
        if 'x' == fita[0]:
            return fita

        if not stack:
            reset_global_variables()
            return fita

        defect = random.randint(0, 99)

        if not epsilon_transition():
            if not fita and stack:
                epsilon_transition()
                reset_global_variables()
                return fita

        if not tape_transition(fita):
            reset_global_variables()
            return fita

    return fita

def Q0():
    global stack
    return populate(push_v="S")

def Q1(fita):
    global stack
    Q0()
    fita = separa_elementos(fita)
    fita = transitions(fita)        
            
    return fita

def Qf(fita):
    print("blablabla alguma coisa modelo do carro")
    return 0

def Qs(fita,pilha):
    print("Erro na fita peça defeituosa")
    print(fita) # onde a fita parou
    print(pilha) # estado da pilha quando deu erro
    return 0


def automata(fita):
    global stack
    initial_stack = stack.copy()
    print(initial_stack)
    Q0()
    a = True
    print(stack)
    while not fita == []:
        result = Q1(fita)
        print(result)
        initial_stack = stack.copy()
        if result is None and initial_stack == []:
            Qf()
            break
        if result[0] == 'x':
            Qs(result,pilha=initial_stack)
            break

    return 0

def add_erro(fita):
    #Encontrar os indices onde os erros n devem ocorrer
    
    indices_sem_erro = [i for i, char in enumerate(fita) if char in ('a', 'b', 'c', 'd', 'a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2')]
    
    
    for i in range(indices_sem_erro[-1] + 1, len(fita)):
        if random.random() < 0.2:
            fita[i] = 'x'
    
    return fita

def Montagem():
    while True:
        print("Qual carro deseja fazer?\n")
        print("A\n")
        print("B\n")
        print("C\n")
        print("D\n")
        carro = input()
        if carro == "A":
            print("Escolha um modelo\n")
            print("EX\n")
            print("GTX\n")
            modelo = input()
            print("\Tamanho do lote:\n")
            Tamanho = input()


        if carro == "B":
            print("Escolha um modelo\n")
            print("EX\n")
            print("GTX\n")
            modelo = input()
            print("\Tamanho do lote:\n")
            Tamanho = input()

        if carro == "C":
            print("Escolha um modelo\n")
            print("EX\n")
            print("GTX\n")
            modelo = input()
            print("\Tamanho do lote:\n")
            Tamanho = input()

        if Carro == "D":
            print("Escolha um modelo")
            print("EX\n")
            print("GTX\n")
            modelo = input()
            print("\Tamanho do lote:\n")
            Tamanho = input()

    return Tamanho, 


def improviso(cont, fita):
    while cont >= 0:
        automata(fita)
        cont = cont - 1
    return 0

fita = "aa1r1m1"
fita = separa_elementos(fita)

improviso(cont=100, fita=fita)

Symbols = ['a', 'b', 'c', 'd', 'a1', 'a2', 'b1', 'b2', 'c1', 'c2', 'd1', 'd2', 'r1', 'r2', 'm1', 'm2', 'v', 'f', 'x', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']
fita = "aa1"
fita = separa_elementos(fita)

automata(fita) #teste da construção do automato
