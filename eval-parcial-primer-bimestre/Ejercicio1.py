"""Realizar un programa en Java que permita ingresar por teclado la longitud y la anchura de una
   habitación, realizar los procesos respectivos que permita obtener la superficie de la misma,
   además se debe presentar en pantalla el valor de la superficie, finalmente tomar en
   consideración que se debe presentar el valor con 3 decimales."""
#ingreso de datos
longitud = float(input("Ingrese lalongitud del cuarto : "))
anchura = float(input("Ingrese el ancho del cuarto: "))
#proceso
superficie = round(longitud*anchura, 3) 
#salida
print("La superficie del cuarto es:"format.(superficie)) 
