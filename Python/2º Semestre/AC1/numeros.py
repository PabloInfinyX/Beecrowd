# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: pablo.moreira@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    c = 0
    for i in range(1, n+1):
        if n % i == 0:
            c += 1
    if c == 2:
        return(True)
    else:
        return(False)


def lista_primos(n):
    numeros = []
    for primo in range(1, n):
        div = 0
        for n in range(1, primo+1):
            if (primo % n == 0):
                div = div + 1
        if (div == 2):
            numeros.append(primo)
    return(numeros)


def conta_primos(s):
    dict = {}
    for numero in s:
        if eh_primo(numero):
            if numero in dict:
                valor = dict[numero] + 1
                dict.update({numero: valor})
            else:
                dict[numero] = + 1
    return(dict)


def eh_armstrong(n):
    tam = len(str(n))
    sum = 0
    div = n
    while div > 0:
        d = div % 10
        sum = sum + (d ** tam)
        div = div // 10
    if n == sum:
        return (True)
    else:
        return (False)


def eh_quase_armstrong(n):
    tam = len(str(n))
    sum = 0
    div = n
    while div > 0:
        d = div % 10
        sum = sum + (d ** tam)
        div = div // 10
    if n-1 == sum:
        return(True)
    else:
        return(False)


def lista_armstrong(n):
    lista = []
    for v in range(0, n):
        if eh_armstrong(v):
            lista.append(v)
    return(lista)


def eh_perfeito(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    if s == n:
        return(True)
    else:
        return(False)


def lista_perfeitos(n):
    lista = []
    for i in range(1, n):
        if eh_perfeito(i):
            lista.append(i)
    return(lista)
