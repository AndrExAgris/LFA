from helpers import separa_elementos
from stack import stack
from pushdown_automata import automata

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

        if carro == "D":
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

improviso(cont=1, fita=fita)