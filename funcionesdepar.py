import os
import numpy as np
def llenarMatriz(mat):
    p=1
    for i in range(10):
        for j in range(4):
            mat[i,j]=p
            p+=1
def valiaOp(op):
    while(True):
        try:
            op=int(input("   Elija opcion: "))
            if(op>=1 and op<=5):
                break
            else:
                print("Debe ingresar opcion entre 1 y 5")
        except ValueError:
            print("Debe ser un numero entero")
    return op
def mostrarDisponibles(piso):
    os.system("cls")
    for i in range(10):
        print("\n") 
        for j in range(4):
            if(j==1):
                print("\t",piso[i,j], end="        ")
            else:
                print("\t",piso[i,j], end="    ")
    print("\n\n")
    
def validaDepartamento():
   departamento=0
   while True:
        try: 
            departamento=int(input("Ingrese numero de departament 1-4: "))
            if (departamento>=1 and departamento<=4):
                break
            else:
                print(" Error.. ingrese departamento entre  1 y 4")
        except ValueError:
            print(" Error.. ingrese departamento entre  1 y 4")
   return departamento
def buscarDisponible(piso, departamento):
    for x in range(10):
        for i in range(4):
            if (departamento==piso[x,i]):
                return True
    return False 
def comprardepartamento(piso, departamento):
    for x in range(10):
        for i in range(4):
            if (piso[x,i]==piso):
                piso[x,i]=0          
                if i==0 or i==3:
                    pago=3800
                elif i==1 or i==2:
                    pago=3000
    return pago
def mostarListadoDeCompradores(piso,departamento):
     print
def totalVenta(piso):
    suma=0
    for x in range(10):
        for i in range(4):
            if (piso[x,i]==0):
                if (i==0 or i==3):
                    suma+=0
                elif (i==1 or i==2):
                    suma+=0
    return suma
