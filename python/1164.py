def perfeito(n):
    i=1
    soma=0
    while i<n:
        if n%i==0:
            soma+=i
        i+=1
    return soma==n
    
qtd=int(input())
mais_um=1

while mais_um<=qtd:
    n=int(input())
    if perfeito(n):
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')
    mais_um+=1