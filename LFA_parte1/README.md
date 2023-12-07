# LFA
## Trabalho Final de LFA - Parte 1
Implementação de um simulador de um PDA (pushdown automata).

Linguagem: Python 3.11.6
Bibliotecas utilizadas: subprocess (para realizar comandos de sistema via Python)
Dependências: graphviz (sudo apt install graphviz)

## Inputfile
O input file segue uma estrutura simples: elementos de um mesmo grupo são separados por um espaço e grupos são separados por linhas.
Exemplo:

```q0 q1 qf #estados

a b #alfabeto da fita

B #simbolos da pilha 

δ : #transiçoes
q0 a ε B q0
q0 b B ε q1
q0 ? ? ε qf
q1 b B ε q1
q1 ? ? ε qf

q0 #estado inicial

qf #estados finais
```
Repare que as transições, como caso especial, não têm linhas as dividindo. Outro fator importante para o inputfile são caracteres reservados, sendo `ε` a palavra vazia e `?` a transição vazia.

## Funcionamento
- Com o diretório LFA aberto, execute ```python3 pda.py```.
- Em seguida, o código pedirá por uma fita. Esta deve ser digitada sem espaços, por exemplo: `aaabbb`.
- Para cada passo do autômato, ele esperará uma entrada do usuário para gerar a próxima imagem do autômato com a transição atual destacada em vermelho.
- Por fim, o simulador imprimirá no terminal se a fita foi aceita ou não. Caso não seja aceita, a imagem do autômato permanecerá como a última entrada aceita da fita.


