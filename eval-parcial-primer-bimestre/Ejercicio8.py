"""Ingresar por teclado tres variables, dichas variables siempre tendrán como valores letras
mayúsculas de abecedario. 
Sabiendo que por ejemplo la letra “E” es menor que la letra “P”; establezca una solución que
permita determinar ¿Cuál de las tres letras ingresadas, aparece primero en el abecedario ?
Ejemplo: Si el usuario ingresa:
v1 = “Z”
v2 = “B”
v3 = “C”"""
#ingreso de datos
no1 =  str ( input ( " Ingrese una letra: " ))
no1 = no1.upper ()         
v1 = no1 [ 0 ]              

no2 =  str ( input ( " Ingrese una letra: " ))
no2 = no2.upper ()          
v2 = no2 [ 0 ]               

no3 =  str ( input ( " Ingrese una letra: " ))
no3 = no3.upper ()          
v3 = no3 [ 0 ]               
# salida
if (v1 < v2 y v1 < v3):
    print ( " La primera letra que aparece en el abecedario es {} " .format (v1))
else :
    if (v2 < v1 y v2 < v3):
        print ( " La primera letra que aparece en el abecedario es {} " .format (v2))
    else :
        print ( " La primera letra que aparece en el abecedario es {} " .format (v3))