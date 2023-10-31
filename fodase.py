
f = open("imput", "r")

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

l = f.readline()
termin = l.split("#")[0]
termin = termin.split()
quint.append(termin)



#print(*quint)

gra = open("graphpy.gv", "w+")

gra.write(' digraph X {\n rankdir=LR;\n')

gra.write(' init [shape=point]\n')

for x in quint[4]:
    gra.write(' init -> {} [shape=doublecircle]\n'.format(x))

for x in quint[5]:
    gra.write(' {} [shape=doublecircle]\n'.format(x))

gra.write(' node[shape=circle]\n')

for x in quint[3]:
    gra.write(' {} -> {} [label="{},{},{}"]\n'.format(x[0],x[4], x[1], x[2], x[3]))
gra.write("}\n")

