n=int(input())
i=1
pos=1
maior=n
while i<100:
    i+=1
    n=int(input())
    if n>maior:
        pos=i
        maior=n
print(maior)
print(pos)