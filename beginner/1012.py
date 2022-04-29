l = input().split(" ")
a, b, c = l

triangulo = float(a) * float(c) / 2
circulo = 3.14159 * float(c)**2
trapezio = ((float(a) + float(b)) * float(c)) / 2

print(f'TRIANGULO: {triangulo:.3f}')
print(f'CIRCULO: {circulo:.3f}')
print(f'TRAPEZIO: {trapezio:.3f}')
print(f'QUADRADO: {float(b)*float(b):.3f}')
print(f'RETANGULO: {float(a)*float(b):.3f}')
