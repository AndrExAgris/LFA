# para poder executar o comando(shell) do graphviz que gera o png apartir do dotfile
import subprocess


#uma função que transcreve o automato para o dotfile 
def gendot(graph, current):
    gra = open("automata.dot", "w+")

    gra.write('digraph X {\nrankdir=LR;\n')

    gra.write('init [shape=point]\n')
    gra.write('node[shape=circle]\n')

    for x in graph[4]:
        gra.write('init -> {}\n'.format(x))

    finais = "node[shape=doublecircle] "
    for x in graph[5]:
        finais = finais + x
    gra.write(finais + ";\n")

    gra.write('node[shape=circle]\n')

    #parte da função que, no dot file especifica as trasiçoes e pode destacalas ou não
    for x in graph[3]:
        if current == -1:
            gra.write(' {} -> {} [label="{},{},{}"]\n'.format(x[0], x[4], x[1], x[2], x[3]))
        else:
            if x == current:
                #aqui a aresta destacada é colorida de vermelho
                gra.write(' {} -> {} [label="{},{},{}", color="red"]\n'.format(x[0], x[4], x[1], x[2], x[3]))
            else:
                gra.write(' {} -> {} [label="{},{},{}"]\n'.format(x[0], x[4], x[1], x[2], x[3]))
    gra.write("}\n") 


# começo do codigo em si, iniciando com o carregamento no codigo dos dados no inputfile
f = open("inputfile", "r")

#a sextupla aqui é traatada como um vetor de vetores
ntupla = []

#coleta os estados
l = f.readline()
estados = l.split("#")[0]
estados = estados.split()
ntupla.append(estados)
l = f.readline()

#coleta os elementos do alfabeto
l = f.readline()
alfab = l.split("#")[0]
alfab = alfab.split()
ntupla.append(alfab)
l = f.readline()

#coleta os simbolos da pilha
l = f.readline()
pilha = l.split("#")[0]
pilha = pilha.split()
ntupla.append(pilha)
l = f.readline()

#coleta as transiçoes, cada uma sendo seu proprio vetor
l = f.readline()
trans = []
while (l != "\n"):
    l = f.readline()
    t = [x if x != "''" else '§' for x in l.split()]
    trans.append(t)
trans.pop()
ntupla.append(trans)

#coleta o estado inicial
l = f.readline()
init = l.split("#")[0]
init = init.split()
ntupla.append(init)

#coleta os estados finais
f.readline()
l = f.readline()
termin = l.split("#")[0]
termin = termin.split()
ntupla.append(termin)


#aqui é gerado a primeira imagem do automato
#primeiro chamando a função geradora do dotfile
gendot(ntupla, -1)
#e então executando o comando shel que gera um png apartir do dotfile
command = 'dot -Tpng automata.dot -o graph.png'
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(e.stderr)


# aqui é onde a fita é imputada no sistema
print("Digite a fita (ex1: 'abaaa' ex2: '')")
fita = input()

#criação de um auxiliar de posicionamento da fita, pilha e estado inicial carregado no estado atual
posfita = 0
stack = []
estado = ntupla[4][0]


#aqui faremos uma iteração para cada elemento da fita
for i in fita:
    #uma verificação se o elemento  atual faz parte do alfabeto
    if all(i != item for item in ntupla[1]):
        print(i, " não é aceito pelo autômato \nfita não reconhecida")
        exit()
    
    #entaõ uma comparação com cada transição para verificar aceitação da fita
    for j in ntupla[3]:
        if estado == j[0] and i == j[1]:
            if len(stack) != 0 and (stack[-1] == j[2] or j[2] == "ε"):
                
                if stack[-1] == j[2]:
                    stack.pop()
                if j[3] != "ε":
                    stack.append(j[3])
                estado = j[4]
                posfita += 1
                gendot(ntupla, j)
                command = 'dot -Tpng automata.dot -o graph.png'
                try:
                    subprocess.run(command, shell=True, check=True)
                except subprocess.CalledProcessError as e:
                    print(e.stderr)
                a = input()
                break
            else:
                if j[2] == "ε":
                    if j[3] != "ε":
                        stack.append(j[3])
                    estado = j[4]
                    posfita += 1
                    gendot(ntupla, j)
                    command = 'dot -Tpng automata.dot -o graph.png'
                    try:
                        subprocess.run(command, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        print(e.stderr)
                    a = input()
                    break
        
#caso a fita não possa ser lida completamente ela não é reconhecida
if posfita != len(fita):
    print("fita não reconhecida")
    exit()

#caso a pilha esteja vazia e estiver em um estado final(ou algum com transiçaõ vazia para o final) é reconhecida
if len(stack) == 0:
    if any(estado == item for item in ntupla[5]):
        print("fita reconhecida")
    else:
        for j in ntupla[3]:
            if estado == j[0] and j[1] == "?" and j[2] == "?" and j[3] == "ε":
                if any(j[4] == item for item in ntupla[5]):
                    gendot(ntupla, j)
                    command = 'dot -Tpng automata.dot -o graph.png'
                    try:
                        subprocess.run(command, shell=True, check=True)
                    except subprocess.CalledProcessError as e:
                        print(e.stderr)
                    print("fita reconhecida")
                    break
else:
    print("fita não reconhecida")
