lista = []

tempo_corrida = int(input())
lista.append(tempo_corrida)
contador_tempo = 1

while tempo_corrida > 0:
    tempo_corrida = int(input())
    if tempo_corrida > 0:
        lista.append(tempo_corrida)
        contador_tempo += 1

MEDIA = 0
for num in lista:
    MEDIA += num
MEDIA = MEDIA / contador_tempo

print(f'MEDIA: {MEDIA:.2f}')
lista.append(MEDIA)
for tempo in lista:
    if tempo < MEDIA:
        print(tempo)