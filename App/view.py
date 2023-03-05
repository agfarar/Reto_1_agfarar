"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist as arrlt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
assert cf
from tabulate import tabulate
import traceback
default_limit = 1000 
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control=controller.new_controller()
    return control


def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")
lt.iterator

def load_data(control,sample):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    header= ["Año","Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    data_size=controller.load_data(control)
    sorted_array_list=controller.sort(control['model'])
    print("- "*20) 
    print("Loaded service info:\n")
    print(f'Total loaded titles:{49}\n')
    print(f'Total loaded features:{data_size}\n')
    print("- "*20)
    years=("2012","2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021")
    for year in years:
        mid_list=[]
        for i in lt.iterator(sorted_array_list):
            if i["Año"]==year:
                mid_list+=[i]
        print(tabulate_data(mid_list[:3]+mid_list[-3:], header))
       
def tabulate_data(data_set, header):#Si veo optimo utilizo el sample para los demas requerimientos
    data_set_org=[]
    for i in data_set:
        i=dict([(key,val) for key,val in i.items() if key in header])
        data_set_org.append(i)
    rows=[x.values() for x in data_set_org]
    print(tabulate(rows,headers=header,tablefmt='grid',maxcolwidths=13,maxheadercolwidths=13))

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    header= ["Año","Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    # print(tabulate_data(controller.req_1(control),header))
    print(tabulate_data(controller.req_1(control)['elements'],header))


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    header= ["Año","Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    return tabulate_data(controller.req_2(control)['elements'],header)


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    first_header=["Año", "Codigo sector económico", "Nombre sector económico","Codigo subsector económico","Nombre sector económico","Retenciones del subsector económico","Costos y gastos del subsector económico","Ingresos netos del subsector economico","Saldo a pagar del subsector economico","Saldo a favor del subsector economico"]
    second_header=["Año","Código actividad económica","Nombre actividad económica","Total retenciones","Total ingresos netos", "Total costos y gastos","Total saldo a pagar","Total saldo a favor"]

def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    

    #Primera parte del requerimiento 
    headers=['Año','Código sector económico','Nombre sector económico','Código subsector económico','Nombre subsector económico','total de costos y gastos nómina del subsector económico','total ingresos netos del subsector económico','total costos y gastos del subsector económico','total saldo por pagar del subsector económico']
    lista=controller.req_4(control)
    print(lista)
    # for i in lt.iterator(lista):
    #      if i['key']=='2012':
    #          for j in lt.iterator(i):
    #             if j['key']=='8':
    #                 print(j)
                



def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    """
        Función que imprime la solución del Requerimiento 7 en consola, sample es el numero de cosas que el usuario quiera imprimri
    """
    # TODO: Imprimir el resultado del requerimiento 7
    
    sample = int(input("Cuantos datos desea imprimir por anio? "))
    
    titulos = ["Año","Código actividad económica","Nombre actividad económica", "Código sector económico", "Nombre sector económico", 
               "Código subsector económico", "Nombre subsector económico", "Total ingresos netos", 
               "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]
    
    titulos_fake = ["Año","Código actividad económica","Nombre actividad económica", "Código sector económico", "Nombre sector económico", 
               "Código subsector económico", "Nombre subsector económico", "Total ingresos netos consolidados para el periodo", 
               "Total costos y gastos consolidados para el periodo", "Total saldo por pagar consolidados para el periodo", 
               "Total saldo a favor consolidados para el periodo"]
    
    ao = input("Desde que anio quiere imprimir?")
    
    ax = input("\n Listo, hasta que anio?")
    
    lista_ordenada = controller.req_7(control, ao, ax, sample)
    
    #Este es el proceso de tabulacion estandar que siempre hacemos para que se vea la lista linda y ordenada en el tabulate
    big_table = []
            
    for line in lt.iterator(lista_ordenada):
            
            tabulated_line = []
            
            for title in titulos:
                
                tabulated_line += [line[title]]
                
            big_table += [tabulated_line]
            
    print(tabulate(big_table, headers = titulos_fake, tablefmt= "grid", maxcolwidths= 13, maxheadercolwidths= 13))

def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    sample = int(input("Cuantos datos desea imprimir por anio? "))
    
    
    ao = input("Desde que anio quiere imprimir?")
    
    ax = input("\n Listo, hasta que anio?")
    
    req_8 = controller.req_8(control, ao, ax, sample)
    
    listica = req_8[0]
        
    titulos = ["Código sector económico", "Nombre sector económico", 
               "Código subsector económico", "Nombre subsector económico", "Total impuesto a cargo para el subsector", "Total ingresos netos para el subsector", 
               "Total costos y gastos para el subsector", "Total saldo a pagar para el subsector", "Total saldo a favor para el subsector"]
    
  
    print(tabulate(listica["elements"], headers = titulos, tablefmt= "grid", maxcolwidths= 13, maxheadercolwidths= 13))
    
    top_n_por_anio = req_8[1]
    
    titulos_subsectores = ["Código actividad económica", "Nombre actividad económica", "Total Impuesto a cargo", "Total ingresos netos", "Total costos y gastos", "Total saldo a pagar", "Total saldo a favor"]

    #Aca recorro cada topn del anio para imprimir por cada anio la lista de top n de ese anio
    
    for top in top_n_por_anio:
        
        top_del_subsector = top_n_por_anio.get(top)["size"]
        lista_de_ese_subsector = top_n_por_anio.get(top)
        
        #Este condicional es para adecuar el print, para ver si digo que solo hubo n actividades o decir este fue el top n actividades
        if top_del_subsector == sample:
            
            print("Para el subsector ", top, " estas fueron las ", top_del_subsector, " actividades economicas que mas aportaron: ")

            #Este es el proceso de tabulacion estandar que siempre hacemos para que se vea la lista linda y ordenada en el tabulate
            big_table = []
        
            for line in lt.iterator(lista_de_ese_subsector):
                    
                    tabulated_line = []
                    
                    for title in titulos_subsectores:
                        
                        tabulated_line += [line[title]]
                        
                    big_table += [tabulated_line]
                    
            print(tabulate(big_table, headers = titulos_subsectores, tablefmt= "grid", maxcolwidths= 13, maxheadercolwidths= 13))

        else:
            
             print("Para el subsector ", top, " solo hay ", top_del_subsector, " actividades economicas que aportaron: ")
             
            #Este es el proceso de tabulacion estandar que siempre hacemos para que se vea la lista linda y ordenada en el tabulate
             big_table = []
            
             for line in lt.iterator(lista_de_ese_subsector):
                    
                    tabulated_line = []
                    
                    for title in titulos_subsectores:
                        
                        tabulated_line += [line[title]]
                        
                    big_table += [tabulated_line]
                    
             print(tabulate(big_table, headers = titulos_subsectores, tablefmt= "grid", maxcolwidths= 13, maxheadercolwidths= 13))
# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        try:
            if int(inputs) == 1:
                print("Cargando información de los archivos ....\n")
                data = load_data(control,3)
            elif int(inputs) == 2:
                print_req_1(control)

            elif int(inputs) == 3:
                print_req_2(control)

            elif int(inputs) == 4:
                print_req_3(control)

            elif int(inputs) == 5:
                print_req_4(control)

            elif int(inputs) == 6:
                print_req_5(control)

            elif int(inputs) == 7:
                print_req_6(control)

            elif int(inputs) == 8:
                print_req_7(control)

            elif int(inputs) == 9:
                print_req_8(control)

            elif int(inputs) == 0:
                working = False
                print("\nGracias por utilizar el programa")
                
            else:
                print("Opción errónea, vuelva a elegir.\n")
        except Exception as exp:
            print("ERR:", exp)
            traceback.print_exc()
    sys.exit(0)
