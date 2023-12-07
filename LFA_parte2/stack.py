from helpers import separa_elementos
global stack
stack = []
def populate(pop_v="&", push_v="&"):
    Symbols = ['car_a', 'car_b', 'car_c', 'car_d', 'mod_aa', 'mod_ab', 'mod_ba', 'mod_bb', 'mod_ca', 'mod_cb', 'mod_da', 'mod_db', 'cor_preto', 'cor_vermelho', 'arcond', 'multimidia', 'rodas_estrada', 'rodas_offroad', 'erro', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']

   
    if pop_v != "&":
        pop_v = separa_elementos(pop_v, Symbols)
        for x in pop_v:
            while stack and stack[-1] == x:
                stack.pop()


    if push_v != "&":
        push_v = separa_elementos(push_v, Symbols)
        stack.extend(reversed(push_v))

    return None

def reset_stack():
    global stack
    stack.clear()