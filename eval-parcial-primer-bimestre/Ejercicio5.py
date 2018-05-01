"""Ingresar por teclados 4 calificaciones de un estudiante, encontrar el promedio de las
calificaciones ingresadas. Presentar la puntuación del estudiante en base a la siguiente información:
Media Puntuación
90-100 A
80-89 B
70-79 C
0-69 D
El reporte sería por ejemplo así:
El estudiante con el promedio de calificaciones 70, tiene una puntuación de C."""
#ingreso de datos
c1 =float (input("ingrese la primera calificación:"))
c2 =float(input("ingrese la segunda calificación:"))
c3 =float(input("ingrese la tercera calificación:"))
c4 =float(input("ingrese la cuarta calificación:"))
#proceso
suma = c1 + c2 + c3+ c4;        
prom = suma/4;
#salida 
if(prom>90 and prom<= 100):
     print("El estudiante tiene la calificación de {}\n,tiene una puntuacion de A ".format(prom))
     
        
     if(prom>80 and prom<89):
         print("El estudiante tiene la calificación de {}\n,tiene una puntuacion de B ".format(prom))  
             
         if(prom>70 and prom<79):
             print("El estudiante tiene la calificación de {}\n,tiene una puntuacion de C ".format(prom))  
      
        
             if(prom>0 and prom<69):
                 print("El estudiante tiene la calificación de {}\n,tiene una puntuacion de D ".format(prom)) 