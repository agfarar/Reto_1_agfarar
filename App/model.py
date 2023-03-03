"""
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
#[arrlt.addFirst(sup_code_tuple,x['Código actividad económica']) for x in data_structs['model']['data']['elements'] if x['Código actividad económica'] not in sup_code_tuple['elements']]

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

    years=('2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012')

    codes_sector=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12')

    codes_sub_sector=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')

    list_ord_by_year_and_code=lt.newList(datastructure='ARRAY_LIST')

    for year in years:
        list_by_year=lt.newList(datastructure='ARRAY_LIST')
        list_by_year['key']=year
        for code in codes_sector:

            list_by_code=lt.newList(datastructure='ARRAY_LIST')
            list_by_code['key']=code

            for code_sub in codes_sub_sector:
                list_by_code_sub=lt.newList(datastructure="ARRAY_LIST")
                list_by_code_sub['key']=code_sub

                for element in lt.iterator(data_structs['model']['data']):

                    if element['Año']==year and element['Código sector económico']==code and element['Código subsector económico']==code_sub:
                            lt.addFirst(list_by_code_sub,element)
                if list_by_code_sub['size']!=0:
                    lt.addFirst(list_by_code,list_by_code_sub)
            if list_by_code['size']!=0:
                lt.addFirst(list_by_year,list_by_code)
        lt.addFirst(list_ord_by_year_and_code,list_by_year)
        
        #Año - codigo- sub_codigo
    
#bueno aca la idea es organizar el nuevo diccionario  de acuerdo a los requerimientos 
    for year in lt.iterator(list_ord_by_year_and_code):
        list_by_year=lt.newList(datastructure='ARRAY_LIST')
        list_by_year['key']=year['key']
        for key_sup in lt.iterator(year):
            list_by_code=lt.newList(datastructure='ARRAY_LIST')
            list_by_code['key']=key_sup['key']

            for key_inf in lt.iterator(key_sup):
                list_by_code_sub=lt.newList(datastructure="ARRAY_LIST")
                list_by_code_sub['key']=key_inf['key']

                diccionario={}
                Código_sector_económico=0
                Nombre_sector_económico=0
                Código_subsector_económico=0
                Nombre_subsector_económico=0
                total_costos_y_gastos_nomina=0
                total_ingresos_netos_del_subsector_económico=0
                total_costos_y_gastos_del_subsector_económico=0
                total_saldo_por_pagar_del_subsector_económico=0

                for element in lt.iterator(key_inf):
                    diccionario['Código sector económico']=element['Código sector económico']
                    diccionario['Nombre sector económico']=element['Nombre sector económico']
                    diccionario['Código subsector económico']=element['Código subsector económico']
                    diccionario['Nombre subsector económico']=element['Nombre subsector económico']
                    diccionario['total costos y gastos nomina']=element['Costos y gastos nómina']
                    diccionario['total ingresos netos del subsector económico']=element['Total ingresos netos']
                    diccionario['total costos y gastos del subsector económico']=element['Total costos y gastos']
                    diccionario['total saldo por pagar del subsector económico']=element['Total saldo a pagar']

                
                    # print(element['Costos y gastos nómina'])

                    # print(elements)#aca es el codigo superior
                    # for key in lt.iterator(elements):#aca son los subsectores
                    #     pass
                    # for key in lt.iterator(elements):#ya se tiene la key superior en comun
                    #     print(key)#se evalua la key inferior en comun 
'''
    Año.
    • Código sector económico.
    • Nombre sector económico.
    • Código subsector económico.
    • Nombre subsector económico.
    • El total de costos y gastos nómina del subsector económico.
    • El total ingresos netos del subsector económico.
    • El total costos y gastos del subsector económico.
    • El total saldo por pagar del subsector económico.
    • El total saldo a favor del subsector económico.
    • Las tres actividades económicas que menos aportaron y las tres actividades económicas que más
    aportaron al valor total de costos y gastos de nómina en cada año, en donde cada elemento contendrá la siguiente información:
    o Códigoactividadeconómica.
    o Nombreactividadeconómica. o El total costos y gastos nómina. o El total ingresos netos.
    o El total costos y gastos.
    o El total saldo por pagar.
    o El Total saldo a favor.
 '''
def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


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


