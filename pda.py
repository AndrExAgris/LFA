# Importa a biblioteca subprocess para executar comandos do Graphviz que geram o PNG a partir do dotfile
import subprocess

# Função que gera a representação do autômato no dotfile
def gendot(graph, current):
    # Abre o arquivo "automata.dot" para escrita
    gra = open("automata.dot", "w+")

    # Escreve o cabeçalho do dotfile
    gra.write('digraph X {\nrankdir=LR;\n')

    # Define o estado inicial como um ponto
    gra.write('init [shape=point]\n')
    gra.write('node[shape=circle]\n')

    # Cria transições do estado inicial para os estados iniciais do autômato
    for x in graph[4]:
        gra.write('init -> {}\n'.format(x))

    # Define os estados finais do autômato com forma de duplo círculo
    finais = "node[shape=doublecircle] "
    for x in graph[5]:
        finais = finais + x
    gra.write(finais + ";\n")

    gra.write('node[shape=circle]\n')

    # Parte da função que especifica as transições no dotfile
    # e permite destacar uma transição em vermelho se for a atual
    for x in graph[3]:
        if current == -1:
            gra.write(' {} -> {} [label="{},{},{}"]\n'.format(x[0], x[4], x[1], x[2], x[3]))
        else:
            if x == current:
                # A aresta destacada é colorida de vermelho
                gra.write(' {} -> {} [label="{},{},{}", color="red"]\n'.format(x[0], x[4], x[1], x[2], x[3]))
            else:
                gra.write(' {} -> {} [label="{},{},{}"]\n'.format(x[0], x[4], x[1], x[2], x[3]))
    
    # Fecha o dotfile
    gra.write("}\n")


# Abre o arquivo "inputfile" para leitura
f = open("inputfile", "r")

# Inicializa uma lista ntupla que representará a sextupla do autômato
ntupla = []

# Coleta os estados do autômato
l = f.readline()
estados = l.split("#")[0]
estados = estados.split()
ntupla.append(estados)
l = f.readline()

# Coleta os elementos do alfabeto do autômato
l = f.readline()
alfab = l.split("#")[0]
alfab = alfab.split()
ntupla.append(alfab)
l = f.readline()

# Coleta os símbolos da pilha do autômato
l = f.readline()
pilha = l.split("#")[0]
pilha = pilha.split()
ntupla.append(pilha)
l = f.readline()

# Coleta as transições do autômato, onde cada transição é representada por um vetor
l = f.readline()
trans = []
while (l != "\n"):
    l = f.readline()
    t = [x if x != "''" else '§' for x in l.split()]
    trans.append(t)
trans.pop()
ntupla.append(trans)

# Coleta o estado inicial do autômato
l = f.readline()
init = l.split("#")[0]
init = init.split()
ntupla.append(init)

# Coleta os estados finais do autômato
f.readline()
l = f.readline()
termin = l.split("#")[0]
termin = termin.split()
ntupla.append(termin)

# Fecha o arquivo após a coleta dos dados
f.close()


# Geração da primeira imagem do autômato:
# Primeiro, chamando a função que gera o dotfile
gendot(ntupla, -1)
# Em seguida, executando o comando do Graphviz que gera um arquivo PNG a partir do DOT
command = 'dot -Tpng automata.dot -o graph.png'
try:
    subprocess.run(command, shell=True, check=True)
except subprocess.CalledProcessError as e:
    print(e.stderr)

# Inserção da fita no sistema
print("Digite a fita (ex1: 'abaaa' ex2: '')")
fita = input()

# Criação de auxiliares para posicionar a fita, a pilha e o estado inicial no estado atual
posfita = 0
stack = []
estado = ntupla[4][0]

# Iteração para cada elemento da fita
for i in fita:
    # Verificação se o elemento atual faz parte do alfabeto
    if all(i != item for item in ntupla[1]):
        print(i, " não é aceito pelo autômato \nfita não reconhecida")
        exit()
    
    # Comparação com cada transição para verificar a aceitação da fita
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
        
# Caso a fita não possa ser lida completamente, ela não é reconhecida
if posfita != len(fita):
    print("fita não reconhecida")
    exit()

# Caso a pilha esteja vazia e esteja em um estado final (ou algum com transição vazia para o final), é reconhecida
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
