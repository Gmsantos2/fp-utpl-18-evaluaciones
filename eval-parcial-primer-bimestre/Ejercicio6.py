""" Realizar un programa que permita ingresar el número de mes de un año (1,…,12), en base al
valor ingresado presenta el número de días que tiene ese mes."""
#ingreso de datos
num =  int ( input ( " Ingrese el número del mes: " ))
#proceso
if (num ==  2 ):
     dias =  28
     if (num ==  4  and  num ==  6  and num ==  9  and num ==  11 ):
         dias =  30
else :
      dias =  31
#salida
print ( " El mes {} tiene {} dias \n " .format (num, dias))
