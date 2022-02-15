def trocar(x, y):
    AUX = int()
    if x > y:
        AUX = x
        x = y
        y = AUX
        return(x, y)
    else:
        return(x, y)

A = 10
B = 5
C = 7
D = 1

A, B = trocar(A, B)
B, C = trocar(B, C)
C, D = trocar(C, D)
A, B = trocar(A, B)
B, C = trocar(B, C)
A, B = trocar(A, B)
print(A, B, C, D)