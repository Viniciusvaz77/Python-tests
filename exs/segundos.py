segundos= input("Por favor, entre com o número de segundos que deseja converter: ")
sgds= int(segundos)

a= sgds//86400
segdsrestantes= sgds%86400
b= segdsrestantes // 3600
segsrest= segdsrestantes % 3600
c= segsrest//60
d= segsrest%60

print(int(a),"dias",int(b),"horas",c,"minutos e",d,"segundos.")
