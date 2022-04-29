x = float(input())

if x <= 400:
    nx = x * 1.15
    print(f'Novo salario: {nx:.2f}')
    print(f'Reajuste ganho: {nx - x:.2f}')
    print('Em percentual: 15 %')

if 400.01 <= x <= 800.00:
    nx = x * 1.12
    print(f'Novo salario: {nx:.2f}')
    print(f'Reajuste ganho: {nx - x:.2f}')
    print('Em percentual: 12 %')

if 800.01 <= x <= 1200.00:
    nx = x * 1.10
    print(f'Novo salario: {nx:.2f}')
    print(f'Reajuste ganho: {nx - x:.2f}')
    print('Em percentual: 10 %')

if 1200.01 <= x <= 2000.00:
    nx = x * 1.07
    print(f'Novo salario: {nx:.2f}')
    print(f'Reajuste ganho: {nx - x:.2f}')
    print('Em percentual: 7 %')

if x > 2000.00:
    nx = x * 1.04
    print(f'Novo salario: {nx:.2f}')
    print(f'Reajuste ganho: {nx - x:.2f}')
    print('Em percentual: 4 %')
