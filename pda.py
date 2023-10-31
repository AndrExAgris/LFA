
# lendo a quintupla para um arquivo -------------------------------------------------
f = open("inputfile", "r")

quint = []

l = f.readline()
estados = l.split("#")[0]
estados = estados.split()
quint.append(estados)
l = f.readline()

l = f.readline()
alfab = l.split("#")[0]
alfab = alfab.split()
quint.append(alfab)
l = f.readline()

l = f.readline()
pilha = l.split("#")[0]
pilha = pilha.split()
quint.append(pilha)
l = f.readline()

l = f.readline()
trans = []
while (l != "\n"):
    l = f.readline()
    t = [x if x!="''" else '§' for x in l.split()]
    trans.append(t)
trans.pop()
quint.append(trans)

l = f.readline()
init = l.split("#")[0]
init = init.split()
quint.append(init)

f.readline()
l = f.readline()
termin = l.split("#")[0]
termin = termin.split()
quint.append(termin)

#criando o arquivo do graphviz -------------------------------------------------------
gra = open("graphpy.gv", "w+")

gra.write(' digraph X {\n rankdir=LR;\n')

gra.write(' init [shape=point]\n')

for x in quint[4]:
    gra.write(' init -> {}\n'.format(x))

finais = " node[shape=doublecircle] "
for x in quint[5]:
    finais = finais + x
gra.write(finais + ";\n")

gra.write(' node[shape=circle]\n')

for x in quint[3]:
    gra.write(' {} -> {} [label="{},{},{}"]\n'.format(x[0],x[4], x[1], x[2], x[3]))
gra.write("}\n")


#recebendo a fita -------------------------------------------------------------------
print("Digite a fita (ex: 'abaaa')")
fita = input()

posfita = 0
stack = [] 
estado = quint[4][0]

for i in fita:
    if all(i != item for item in quint[1]):
        print(i, " não é aceito pelo autamato \nfita não reconhecida")
        exit()
    

    for j in quint[3]:
        if estado == j[0]:
            if i == j[1]:
                if len(stack) != 0:   
                    if stack[-1]== j[3]:  
                        stack.pop()
                        if j[2] != "ε":
                            stack.append(j[2])
                        estado = j[4]
                        posfita+=1
                        break
                    elif j[3] == "ε":
                        if j[2] != "ε":
                            stack.append(j[2])
                        estado = j[4]
                        posfita+=1
                        break
                else:
                    if j[3] == "ε":  
                        if j[2] != "?":
                            stack.append(j[2])
                        estado = j[4]
                        posfita+=1
                        break
                print("Fita não reconhecida")
                break
    
if (estado in quint[5]):
    print("Fita reconhecida")
