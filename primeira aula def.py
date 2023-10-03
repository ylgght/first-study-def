def rec(x):
    print('[1] SIM \n [2] NÃO \n Você fez recuperação ?')
    a=int(input())
    if a!=2:
        nr=int(input('Quanto você tirou na Recuperação ?'))
        nrf=nr+x
        print('Sua nota foi de : ', nrf)
        if nrf>7:
            print('Aprovado')
        else:
            print('Reprovado')
    else:
        print('Reprovado')
def nota(x):
    if x >= 7:
        print('Aprovado')
    elif x>=4 and x<7:
        print('Recuperação')
        rec(x)
    else:
        print('Reprovado')
def cal():
    n1=float(input('Qual a nota do primeiro bimestre: '))
    n2=float(input('Qual a nota do segundo bimestre: '))
    n3=float(input('Qual a nota do terceiro bimestre: '))
    n4=float(input('Qual a nota do quarto bimestre: '))

    nf=(n1+n2+n3+n4)/4
    print('Sua nota foi de : ', nf)
    nota(nf)
cal()