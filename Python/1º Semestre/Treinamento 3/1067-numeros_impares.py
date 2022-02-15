X = int(input())
while X < 1 or X > 1000:
    X = int(input())
for num in range(1, X + 1):
    if num % 2 != 0:
        print(num, end = "\n")
