id, qtd=input().split()
id=int(id)
qtd=int(qtd)
id1=1
id2=2
id3=3
id4=4
id5=5
if id==id1:
    print(f'Total: R$ {qtd*4.00:.2f}')
elif id==id2:
    print(f'Total: R$ {qtd*4.50:.2f}')
elif id==id3:
    print(f'Total: R$ {qtd*5.00:.2f}')
elif id==id4:
    print(f'Total: R$ {qtd*2.00:.2f}')
else:
    print(f'Total: R$ {qtd*1.50:.2f}')