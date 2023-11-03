# LFA
## Trabalho Final de LFA parte1
Implementação de um simulador de um PDA(pushdown automata).

Linguagem: Python 3.11.6
Bibliotecas utilizadas: subprocess (para realizar comandos de sistema via python)
Dependencias: graphviz (sudo apt install graphviz)

## Inputfile
O imput file segue uma estrutura simples: elementos de um mesmo grupo são separados por um espaço e grupos são separados por linhas  
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
Reparando que as transições como caso especial não tem linhas as dividindo.
Outro fator importante para o inputfile são caracteres reservados, sendo `ε` como palavra vazia  e `?` como transição vazia.

## Funcionamento
* Com o diretorio LFA aberto executar ```python3 pda.py```.
* Então o codigo pedir por uma fita, esta deve ser digitada sem espaços Ex: `aaabbb`
* Para cada passo do automato ele esperara um imput qualquer do usuario para gerar a proxima imagem do automato com a transição atual sendo destacada em vermelho.
* Por fim o o simulador ira printar no terminal se a fita foi aceita ou não.(caso não seja aceita a imagem do automato permanecera como a ultima entrada aceita da fita)

