n = int(input("Introduce el número de términos para la serie de Fibonacci: "))
while n <= 0:
    print("Por favor, introduce un número entero positivo.")
    n = int(input("Introduce el número de términos para la serie de Fibonacci: "))
serie = [0, 1]
if n == 1:
    serie = [0]
elif n > 2:
    for i in range(2, n):
        serie.append(serie[-1] + serie[-2])
print(f"Serie de Fibonacci hasta {n} términos: {serie}")