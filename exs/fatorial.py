numero = int(input("Digite o valor do fatorial desejado: "))

vezes = numero - 1

if numero == 0 or numero == 1:
    print(1)

else:    
    while vezes != 0:

        fatorialN = numero * vezes

        numero = fatorialN

        vezes = vezes - 1

print(fatorialN)
