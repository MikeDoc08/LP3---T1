def factorial(n)
    if n == 0 or n = 1
        retunr 1
    else:
        retunr n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial()}")
