id=int(input())
soma=0
i=0
while id>=0:
    soma+=id
    i+=1
    id=int(input())
    
print(f'{soma/i:.2f}')