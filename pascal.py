print("Elabprado por Muñoz Molina Luis Ángel y Morales Carpinteyro Brayan Mauricio.")
n = int(input("Introduce el número de filas para el triángulo de Pascal: "))
triangulo = []

for i in range(n):
    fila = [1]
    if len(triangulo) > 0:
        for j in range(len(triangulo[-1]) - 1):
            fila.append(triangulo[-1][j] + triangulo[-1][j + 1])
        fila.append(1)
    triangulo.append(fila)

for fila in triangulo:
    print(fila)
