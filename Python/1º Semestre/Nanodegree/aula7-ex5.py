def SOMAR(X, Y, Z):
    Z = X + Y
    return(X, Y, Z)

def MEDIA(M, N, P):
    M = (N + P) / 2
    M = int(M)
    return(M, N, P)

A = 0
B = 2
C = 4

A, B, C = MEDIA(A, B, C)
B, C, A = SOMAR(B, C, A)
B, C, A = MEDIA(B, C, A)
C, A, B = SOMAR(C, A, B)
C, A, B = MEDIA(C, A, B)
A, B, C = MEDIA(A, B, C)
C, A, B = SOMAR(C, A, B)
C, A, B = MEDIA(C, A, B)
print(A, B, C)