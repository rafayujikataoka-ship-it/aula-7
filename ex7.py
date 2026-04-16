from pilha import Pilha
import pilha

def validar_exp(expressao):
    pilha = Pilha()

    for c in expressao:
        if c == '(':
            pilha.push(c)
        elif c == ')':
            if pilha.vazia():
                return False
            pilha.pop()
    return pilha.vazia()

exp1= '(a+b)*(c-d)'
exp2= '(a+b)*c-d)'
