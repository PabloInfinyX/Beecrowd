Animal1 = input()
Animal2 = input()
Animal3 = input()
if Animal1 == 'vertebrado':
    if Animal2 == 'ave':
        if Animal3 == 'carnivoro':
            print('aguia')
        if Animal3 == 'onivoro':
            print('pomba')
    if Animal2 == 'mamifero':
        if Animal3 == 'onivoro':
            print('homem')
        if Animal3 == 'herbivoro':
            print('vaca')
if Animal1 == 'invertebrado':
    if Animal2 == 'inseto':
        if Animal3 == 'hematofago':
            print('pulga')
        if Animal3 == 'herbivoro':
            print('lagarta')
    if Animal2 == 'anelideo':
        if Animal3 == 'hematofago':
            print('sanguessuga')
        if Animal3 == 'onivoro':
            print('minhoca')
