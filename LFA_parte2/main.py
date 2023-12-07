from helpers import starta_elementos
from stack import stack
from pushdown_automata import automata


def improviso(cont, fita):
    while cont >= 0:
        automata(fita)
        cont = cont - 1
    return 0

fita = "car_a mod_aa cor_preto rodas_estrada arcond"
fita = starta_elementos(fita)

improviso(cont=1, fita=fita)