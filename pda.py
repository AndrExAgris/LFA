
# lendo a ntuplaupla para um arquivo -------------------------------------------------
f = open("inputfile", "r")

ntupla = []

l = f.readline()
estados = l.split("#")[0]
estados = estados.split()
ntupla.append(estados)
l = f.readline()

l = f.readline()
alfab = l.split("#")[0]
alfab = alfab.split()
ntupla.append(alfab)
l = f.readline()

l = f.readline()
pilha = l.split("#")[0]
pilha = pilha.split()
ntupla.append(pilha)
l = f.readline()

l = f.readline()
trans = []
while (l != "\n"):
    l = f.readline()
    t = [x if x!="''" else '§' for x in l.split()]
    trans.append(t)
trans.pop()
ntupla.append(trans)

l = f.readline()
init = l.split("#")[0]
init = init.split()
ntupla.append(init)

f.readline()
l = f.readline()
termin = l.split("#")[0]
termin = termin.split()
ntupla.append(termin)

#criando o arquivo do graphviz -------------------------------------------------------
gra = open("automata.gv", "w+")

gra.write(' digraph X {\n rankdir=LR;\n')

gra.write(' init [shape=point]\n')

for x in ntupla[4]:
    gra.write(' init -> {}\n'.format(x))

finais = " node[shape=doublecircle] "
for x in ntupla[5]:
    finais = finais + x
gra.write(finais + ";\n")

gra.write(' node[shape=circle]\n')

for x in ntupla[3]:
    gra.write(' {} -> {} [label="{},{},{}"]\n'.format(x[0],x[4], x[1], x[2], x[3]))
gra.write("}\n")


#recebendo a fita -------------------------------------------------------------------
print("Digite a fita (ex1: 'abaaa' ex2: '')")
fita = input()

posfita = 0
stack = [] 
estado = ntupla[4][0]

for i in fita:
    if all(i != item for item in ntupla[1]):
        print(i, " não é aceito pelo autamato \nfita não reconhecida")
        exit()
    

    for j in ntupla[3]:
        if estado == j[0] and i == j[1]:
            if len(stack) != 0 and (stack[-1] == j[2] or j[2] == "ε"):   
                if stack[-1] == j[2]:
                    stack.pop()
                if j[3] != "ε":
                    stack.append(j[3])
                estado = j[4]
                posfita+=1
                break
            else:
                if j[2] == "ε":  
                    if j[3] != "ε":
                        stack.append(j[3])
                    estado = j[4]
                    posfita+=1
                    break
            print("Fita não reconhecida")
            exit()

if len(stack) == 0:
    if any(estado == item for item in ntupla[5]):
        print("fita reconhecida")
    else:
        for j in ntupla[3]:
            if estado == j[0] and j[1] == "?" and j[2] == "?" and j[3] == "ε":
                if any(j[4] == item for item in ntupla[5]):
                    print("fita reconhecida")
                    break
else:
    print("fita não reconhecida")
