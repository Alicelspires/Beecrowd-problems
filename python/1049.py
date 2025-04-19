def animal(p1, p2, p3):
    if p1=='vertebrado':
        if p2=='ave':
            if p3 =='carnivoro':
                print('aguia')
            else:
                print('pomba')
        else:
            p2=='mamifero'
            if p3 =='onivoro':
                print('homem')
            else:
                print('vaca')
    else:
        p1=='invertebrado'
        if p2 == 'inseto':
            if p3=='hematofago':
                print('pulga')
            else:
                print('lagarta')
        else:
            p2 =='anelideo'
            if p3=='hematofago':
                print('sanguessuga')
            else:
                print('minhoca')
p1=input()
p2=input()
p3=input()
animal(p1, p2, p3)