from gettext import npgettext
import os
import numpy as np
import funcionesdepar as fn
piso=np.empty([10,4], type(int))
fn.llenarMatriz(piso)
os.system("cls")
op=0
departamento=0
while(op!=5):
    os.system("cls")
    print("             Casa Feliz              ")
    print("        **********************  ")
    print("1.	Mostrar departamentos disponibles 	")
    print("2.	Comprar departamento                  ")
    print("3.	Ver listado de compradores                    ")
    print("4.	mostrar ganancia totales                 ")
    print("5.	Salir                           ")
    op=fn.valiaOp(op)
    if(op==1):
        fn.mostrarDisponibles(piso)
        os.system("pause")
    if(op==2):
        fn.mostrarDisponibles(piso)
        departamento=fn.validaDepartamento
        comprueba= fn.buscarDisponible(piso,departamento)
        if comprueba:     
            print("El departamento esta disponible!!")
            pagar=fn.comprardepartamento(piso, departamento)
            print("\t Usted va a cancelar: ", pagar)
        else: 
            print("\t El asiento no esta disponible")
        os.system("pause")
    if(op==3):
        departamento=fn.validaDepartamento()
        listado=fn.mostarListadoDeCompradores(piso,departamento)
       
       
        os.system("pause")
    if op==4:
        suma=0
        suma=fn.totalVenta(piso)
        if (suma==0):
            print("\t No hay departamentos vendidos")
        else:
            print("\t El total vendido $ es: ", suma)
        os.system("pause")
    if(op==5):
        print("\tVuelva pronto.,Matias reveco 11/07/2023")

