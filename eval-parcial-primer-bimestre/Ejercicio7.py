"""Un empresa paga a sus vendedores de la siguiente manera:
Sueldo fijo $ 360.40 más un porcentaje de las ventas realizadas en el mes.
Si las ventas fueron menores o iguales a $ 500, el porcentaje es de 5%
Si las ventas fueron mayores a $ 500 y menores o iguales a $1000, el porcentaje es de 8%
Si las ventas fueron mayores a $ 1000 y menores o iguales a $5000, el porcentaje es de 10%
Si las ventas fueron mayores a $ 5000, el porcentaje es de 15%
Ingresar el valor de las ventas de un empleado y calcular su sueldo en base la información dada."""
#Ingreso de datos
sfijo = 360.40
ventas =  float ( input ( "Ingrese el valor en dolares de las ventas mensuales de el empleado x : " ))
#proceso
if (ventas <=  500 ):
     porc = ventas *  0.05
     ntotal = sfijo + porc
    
     if (ventas >  500  and ventas <=  1000 ):
         porc = ventas *  0.08
         ntotal = sfijo + porc
    
         if (ventas >  1000  and ventas <=  5000 ):
             porc = ventas *  0.10
             ntotal = sfijo + porc
    
             if(ventas > 5000):
                 porc = ventas *  0.15
                 ntotal = sfijo + porc
# salida
print(" El sueldo del empleado x es de: {} USD \n ".format(ntotal))