n_casos=int(input())
for i in range(n_casos):
    n=int(input())
    qtd=0
    p=1
    while p <= n and qtd < 2:
        if n%p==0 :
            qtd+=1
        p+=1
    if p > n:
        print(f'{n} eh primo')
    else:
        print(f'{n} nao eh primo')
    i+=1