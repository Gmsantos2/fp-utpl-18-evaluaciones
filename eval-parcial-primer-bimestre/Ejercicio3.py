""" Realizar un programa que permita ingresar un valor en segundos, luego realizar un proceso que
    permita presentar el valor en minutos y segundos del valor dado. Ejemplo:
    100 segundos es igual a 1 minuto y 40 segundos"""
#ingreso de datos 
minut=0
seg = int(input("Ingrese los segundos: "))
num=seg
#proceso
while(num > 60):
    minut = minut + 1
    num = num - 60
#salida
print("{} segundos es igual a {} minutos y {} segundos\n".format(seg, minut, num))