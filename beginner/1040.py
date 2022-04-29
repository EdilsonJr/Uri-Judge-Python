x = input().split()
n1, n2, n3, n4 = x
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + n4) / 10

if media >= 7:
    print(f'Media: {media:.1f}')
    print('Aluno aprovado.')
elif media < 5:
    print(f'Media: {media:.1f}')
    print('Aluno reprovado.')
else:
    print(f'Media: {media:.1f}')
    print('Aluno em exame.')
    n5 = float(input())
    mf = (media + n5) / 2
    print(f'Nota do exame: {n5:.1f}')
    if mf >= 5:
        print('Aluno aprovado.')
        print(f'Media final: {mf:.1f}')
    else:
        print('Aluno reprovado.')
        print(f'Media final: {mf:.1f}')
