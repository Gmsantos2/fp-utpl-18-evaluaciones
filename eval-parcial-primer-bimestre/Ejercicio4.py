"""Dado el siguiente sistema de ecuaciones:
ax + by = c
dx + ey = f
resolverlo aplicando las siguientes formulas:
x = (c*e-b*f)/(a*e-b*d)
y = (c*e-b*f)/(a*e-b*d)
Presentar en pantalla los valores de x y y"""
#ingreso de datos
a = float(input("Ingrese a: "))
b = float(input("Ingrese b: "))
c = float(input("Ingrese c: "))
d = float(input("Ingrese d: "))
e = float(input("Ingrese e: "))
f = float(input("Ingrese f: "))
#proceso
x = (c*e-b*f)/(a*e-b*d)
y = (c*e-b*f)/(a*e-b*d)
#salida
print("el valor de x es:{}  , y el valor de y es:{}\n ".format(round(x, 3), round(y, 3)))