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
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
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


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    data_size=controller.load_data(control)
    print("- "*15) 
    print("Loaded service info:\n")
    print(f'Total loaded titles:{49}\n')
    print(f'Total loaded features:{data_size}\n')
    print("- "*15)
    sorted_array_list=controller.sort(control["model"])
    sample=3
    titulos = ["Año","Código actividad económica","Nombre actividad económica","Código sector económico","Nombre sector económico","Código subsector económico","Nombre subsector económico","Total ingresos netos","Total costos y gastos","Total saldo a pagar","Total saldo a favor"]
    tabulate_table(sorted_array_list, titles = titulos, pos = 1, first_and_last = True,  sample =3, printable= False, tablefmt= "grid", maxcolwidths=13, maxheadercolwidths= 13)

def tabulate_table(table, titles: list, pos: int, first_and_last: bool, sample: int, printable: bool, tablefmt: str, maxcolwidths: int, maxheadercolwidths: int):
    
    '''table vendria siendo control, esta funcion tabula lo que sea basicamente'''
    if tablefmt == None:
    
        tablefmt = "grid"
        
    if maxheadercolwidths == None:
        
        maxheadercolwidths = 13
        
    if maxcolwidths == None:
        
        maxcolwidths = 13
        
    if pos == None:
        
        pos = 1
    
    if sample == None:
        
        table = table
        
    else:
        
        if first_and_last == True:
        
            last_table  = lt.subList(table, lt.size(table)- (sample-1), sample)
            first_table = lt.subList(table, 1, sample)
            
        else: 
            
            table = lt.subList(table, pos, sample)
        
    if first_and_last == False and printable == False:
        
        big_table = []
            
        for line in lt.iterator(table):
            
            tabulated_line = []
            
            for title in titles:
                
                tabulated_line += [line[title]]
                
            big_table += [tabulated_line]
            
            print(tabulate(big_table, headers = titles, tablefmt= tablefmt, maxcolwidths= maxcolwidths, maxheadercolwidths= maxheadercolwidths))

    elif first_and_last == True:
        
        big_table_first = []
            
        for line in lt.iterator(first_table):
            
            tabulated_line = []
            
            for title in titles:
                
                tabulated_line += [line[title]]
                
            big_table_first += [tabulated_line]
            
        big_table_last = []
            
        for line in lt.iterator(last_table):
            
            tabulated_line = []
            
            for title in titles:
                
                tabulated_line += [line[title]]
                
            big_table_last += [tabulated_line]
        
        print(tabulate(big_table_first, headers = titles, tablefmt= tablefmt, maxcolwidths= maxcolwidths, maxheadercolwidths= maxheadercolwidths))
        print(tabulate(big_table_last, headers = titles, tablefmt= tablefmt, maxcolwidths= maxcolwidths, maxheadercolwidths= maxheadercolwidths))
    elif printable == True:
        
        big_table = []
        
        for anio in table:
                            
            line = table.get(anio)
                            
            tabulated_line = []
            
            for key in line:
                                    
                if key in titles:
                    
                    tabulated_line += [line.get(key)]
                    
                                
            big_table += [tabulated_line]
            
            
                                
        print(tabulate(big_table, headers = titles, tablefmt= tablefmt, maxcolwidths= maxcolwidths, maxheadercolwidths= maxheadercolwidths))


    else:
        
        raise KeyError
    
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
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


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
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


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
                data = load_data(control)
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
