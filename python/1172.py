x=[]
for i in range(10):
    n=int(input())
    x.append(n)
    if x[i] <=0:
        x[i]=1
    print(f'X[{i}] = {x[i]}')