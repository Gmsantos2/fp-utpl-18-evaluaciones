"""Ingresar por teclado la variables: x,y,z , en base a las mismas realizar la siguiente operación:
   m = (x+(y/z))/(x-(y/z))
   y finalmente presentar en pantalla el siguiente reporte:
   El valor de m, en base a las variables:
   x = 10.2
   y = 9.2
   z = 8.2
  da como resultado:
  m = ? """
#ingreso de datos
x = float(input("Ingresar x: "))
y = float(input("Ingresar y: "))
z = float(input("Ingresar z: "))
#proceso
m = (x+(y/z))/(x-(y/z))
#salida
print("El valor de m, en base a las variables :" );
print(+x)
print(+y)
print(+z)
print("da como resultado:")
print(round(+m,3))