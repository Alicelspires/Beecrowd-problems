V=int(input())
for i in range(10):
    if i == 0:
        print(f'N[0] = {V}')
    else:
        V*=2
        print(f'N[{i}] = {V}')