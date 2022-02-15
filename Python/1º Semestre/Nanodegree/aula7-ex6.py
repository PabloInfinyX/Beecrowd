def SOMAR(X, Y, Z):
    Z = X + Y
    return(X, Y, Z)

def MEDIA(M, N, P):
    M = (N + P) / 2
    M = int(M)
    return(M, N, P)

def TROCAR(X, Y):
    AUX = int()
    if X > Y:
        AUX = X
        X = Y
        Y = AUX
        return(X, Y)
    else:
        return(X, Y)

A, B, C = 1, 2, 3

B, C, A = MEDIA(B, C, A)
B, C, A = SOMAR(B, C, A)
B, C, A = MEDIA(B, C, A)
A, B = TROCAR(A, B)
A, B, C = SOMAR(A, B, C)
A, B, C = MEDIA(A, B, C)
A, B = TROCAR(A, B)
A, B, C = MEDIA(C, A, B)
print(A, B, C)