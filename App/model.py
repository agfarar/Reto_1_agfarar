﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.DataStructures import arraylist as arrlt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos

def new_data_structs():
    """
    Inicializa las estructuras de datos del modelo. Las crea de
    manera vacía para posteriormente almacenar la información.
    """
    #TODO: Inicializar las estructuras de datos
    data_structs={"data":lt.newList(datastructure="ARRAY_LIST")}
    return data_structs

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    data_structs=lt.addLast(data_structs["model"]["data"],data)
    return data_structs

# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    data={'id':id,'info':info}
    return data


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pos_data=lt.isPresent(data_structs["data"],id)
    if pos_data>0:
        data=lt.getElement(data_structs["data"],pos_data)
        return data
    return None


def data_size(data_structs):
    """
    Retorna el tamaño de la lista de datos
    """
    #TODO: Crear la función para obtener el tamaño de una lista
    return lt.size(data_structs["data"])

def compar_fun_or_load_data(business_1, business_2): 
    """
    Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2, en caso de que sean iguales tenga en cuenta el código de la actividad económica, de lo contrario devuelva falso (False).
    Args:
    impuesto1: información del primer registro de impuestos que incluye el “Año” y el
    “Código actividad económica”
            impuesto2: información del segundo registro de impuestos que incluye el “Año” y el
            “Código actividad económica”
    """ 
    if business_1["Año"] < business_2["Año"]:
        retorno = True
    elif business_1["Año"] == business_2["Año"]:
        if business_1["Código actividad económica"] < business_2["Código actividad económica"]:
           retorno = True
        else: 
            retorno = False
    else:
        retorno = False
        
    return retorno

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    #Primera tabla
    
    #Sumatoria del primero 
    "El total de costos y gastos nómina del subsector económico.:  Sector_economico: Costos y gastos nómina "
    #SOLO SON 25 sub-sectores economicos
    years=('2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012')

    sup_code=lt.newList(datastructure='ARRAY_LIST')
    [arrlt.addFirst(sup_code,x['Código actividad económica']) for x in data_structs['model']['data']['elements'] if x['Código actividad económica'] not in sup_code['elements']]
    list_ord_by_year_sup_code=lt.newList(datastructure='ARRAY_LIST')
    for year in years:
        s_code_list_by_year=lt.newList(datastructure='ARRAY_LIST')
        for s_code in sup_code['elements']:
            for line in arrlt.iterator(data_structs["model"]["data"]):
                if line["Año"]==year and line["Código actividad económica"]==s_code:
                    arrlt.addFirst(s_code_list_by_year,line)
        s_code_list_by_year['key']=year
        # arrlt.addFirst(list_ord_by_year_sup_code,s_code_list_by_year)
        for i_code in range(1,26):
            pass
    return list_ord_by_year_sup_code






def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs,year:str):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    primero= lt.newList(datastructure="ARRAY_LIST")
    datos=data_structs["model"]["data"]["elements"]
    for iterador in datos:
        if year == iterador["Año"]:
            lt.addLast(primero,iterador)
    final=sort_ingresos(primero)
    return final

def ordenar_ingresos(valor1,valor2)->bool:
    if valor1>valor2:
        return True
    else:
        return False
    
def sort_ingresos(lst):

    sectores=lt.newList(datastructure="ARRAY_LIST")

    subsectores=lt.newList(datastructure="ARRAY_LIST")

    actividades=lt.newList(datastructure="ARRAY_LIST")

    for orden_sec in lst["elements"]:
        presente=lt.isPresent(sectores,orden_sec["Nombre sector económico"])

        if presente==0:
            tupla={"Código actividad económica": orden_sec["Código actividad económica"],"Nombre actividad económica": orden_sec["Nombre actividad económica"],"Total ingresos netos": orden_sec["Total ingresos netos"],"Total costos y gastos": orden_sec["Total costos y gastos"],"Total saldo a pagar": orden_sec["Total saldo a pagar"],"Total saldo a favor": orden_sec["Total saldo a favor"]}
            print(tupla,"TUPLA")
            todo={"Nombre sector económico": orden_sec["Nombre sector económico"],"Código sector económico": orden_sec["Código sector económico"],"Total ingresos netos": orden_sec["Total ingresos netos"],"Total costos y gastos": orden_sec["Total costos y gastos"],"Total saldo a pagar": orden_sec["Total saldo a pagar"],"Total saldo a favor": orden_sec["Total saldo a favor"],
                  "Subsectores":lt.addLast(sectores["Subsectores"],{"Nombre subsector económico": orden_sec["Nombre subsector económico"],"Código subsector económico": orden_sec["Código subsector económico"],"Total ingresos netos": orden_sec["Total ingresos netos"],"Total costos y gastos": orden_sec["Total costos y gastos"],"Total saldo a pagar": orden_sec["Total saldo a pagar"],"Total saldo a favor": orden_sec["Total saldo a favor"],
                  "Actividades":lt.addLast(sectores["Subsectores"]["Actividades"],tupla)})}
        
            lt.addLast(sectores,todo)
        else:
            sectores[presente]["Total ingresos netos"] += orden_sec["Total ingresos netos"]
            sectores[presente]["Total costos y gastos"] += orden_sec["Total costos y gastos"]
            sectores[presente]["Total saldo a pagar"] += orden_sec["Total saldo a pagar"]
            sectores[presente]["Total saldo a favor"] += orden_sec["Total saldo a favor"]
            presente_sub= lt.isPresent(sectores[presente],orden_sec["Nombre subsector económico"])

            if presente_sub == 0:
                tupla={"Código actividad económica": orden_sec["Código actividad económica"],"Nombre actividad económica": orden_sec["Nombre actividad económica"],"Total ingresos netos": orden_sec["Total ingresos netos"],"Total costos y gastos": orden_sec["Total costos y gastos"],"Total saldo a pagar": orden_sec["Total saldo a pagar"],"Total saldo a favor": orden_sec["Total saldo a favor"]}
                mitad={"Nombre subsector económico":orden_sec["Nombre subsector económico"],"Código subsector económico": orden_sec["Código subsector económico"],"Total ingresos netos": orden_sec["Total ingresos netos"],"Total costos y gastos": orden_sec["Total costos y gastos"],"Total saldo a pagar": orden_sec["Total saldo a pagar"],"Total saldo a favor": orden_sec["Total saldo a favor"],"Actividades":tupla}
                lt.addLast(subsectores[presente]["Sectores"],mitad)
            
            else:
                sectores[presente][presente_sub]["Total ingresos netos"] += orden_sec["Total ingresos netos"]
                sectores[presente][presente_sub]["Total costos y gastos"] += orden_sec["Total costos y gastos"]
                sectores[presente][presente_sub]["Total saldo a pagar"] += orden_sec["Total saldo a pagar"]
                sectores[presente][presente_sub]["Total saldo a favor"] += orden_sec["Total saldo a favor"]
                tuplita={"Código actividad económica": orden_sec["Código actividad económica"],"Nombre actividad económica": orden_sec["Nombre actividad económica"],"Total ingresos netos": orden_sec["Total ingresos netos"],"Total costos y gastos": orden_sec["Total costos y gastos"],"Total saldo a pagar": orden_sec["Total saldo a pagar"],"Total saldo a favor": orden_sec["Total saldo a favor"]}
                lt.addLast(sectores[presente][presente_sub]["Actividades"],tuplita)
                quk.sort(sectores[presente][presente_sub]["Actividades"],ordenar_ingresos)
    return sectores








def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    if data_1["id"] > data_2["id"]:
        return 1
    elif data_1["id"] < data_2["id"]:
        return -1
    else:
        return 0

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    return data_1["id"] > data_2["id"]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    return quk.sort(data_structs,compar_fun_or_load_data)


