Symbols = ['car_a', 'car_b', 'car_c', 'car_d', 'mod_aa', 'mod_ab', 'mod_ba', 'mod_bb', 'mod_ca', 'mod_cb', 'mod_da', 'mod_db', 'cor_preto', 'cor_vermelho', 'arcond', 'multimidia', 'rodas_estrada', 'rodas_offroad', 'erro', 'S', 'A', 'B', 'C', 'D', 'A1', 'A2', 'B1', 'B2', 'C1', 'C2', 'D1', 'D2']

def starta_elementos(fita, Symbols=Symbols):
    elementos = fita.split()
    new_elementos = arruma_symbols(elementos, Symbols)
    return new_elementos

def separa_elementos(fita, Symbols=Symbols):
    elementos = fita
    new_elementos = arruma_symbols(elementos, Symbols)
    return new_elementos



def arruma_symbols(elementos, Symbols=Symbols):
    new_elementos = []
    aux = False

    for x in range(len(elementos)):
        if aux:
            aux = False
            continue

        if x + 1 >= len(elementos):
            new_elementos.append(elementos[x])
            return new_elementos

        a = elementos[x] 
        if a in Symbols:
            new_elementos.append(a)
            aux = True
        else:
            new_elementos.append(elementos[x])

    return new_elementos