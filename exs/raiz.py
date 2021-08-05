import math

a= float(input("Valor de A: "))
b= float(input("Valor de B: "))
c= float(input("Valor de C: "))

delts= b**2-4*a*c
pog = "S"

while pog == "S":
    if delts==0:
        raizum= (-b+math.sqrt(delts)) /(2*a)	
        print("A unica raiz é:",raizum)
    elif delts<0:
        print("Essa equação não possui raizes reais.")
    else:
        raizum= (-b+math.sqrt(delts))/(2*a)
        raizdois= (-b-math.sqrt(delts))/(2*a)

        print("A primeira raiz é",raizum)
        print("A segunda raiz é",raizdois)

        pog = input("Deseja continuar?(S/N): ")




