n1,n2,n3,n4=input().split()
n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)
a=(n1*2+n2*3+n3*4+n4)/10
print(f'Media: {a:.1f}')
if a >= 7.0:
    print('Aluno aprovado.')
elif a < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    
    nota_exame=float(input())
    print(f'Nota do exame: {nota_exame}')
    recalculo = (a + nota_exame)/2
    if recalculo >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {recalculo}')