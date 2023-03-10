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

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    data_structs=lt.addLast(data_structs["model"]["data"],data)
    return data_structs

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    data={'id':id,'info':info}
    return data

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

def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    mayor_saldo_anios = ("2012","2013","2014","2015","2016","2017", "2018", "2019", "2020", "2021")
    lista=lt.newList(datastructure="ARRAY_LIST")
    #TODO podrias hacer una sublkista por cada anio y en cada sublista hacer sort por el criterio de total saldo a pagar y escoger el primer elemento
    for anio in mayor_saldo_anios:
        mayor = None
        for line in lt.iterator(data_structs['model']['data']):
            #esta condicion es porq no quiero q me recorra toda la lista si no solo en las q en el anio es el mismo q estoy iterando
            if line["Año"] == anio:
                if mayor == None:
                    mayor = line
                else: 
                    if line["Total saldo a pagar"] > mayor["Total saldo a pagar"]: 
                        mayor = line
                    else: 
                        mayor = mayor       
        lt.addLast(lista,mayor)
    return lista
    
def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    mayor_saldo_favor_anios = ("2012","2013","2014","2015","2016","2017", "2018", "2019", "2020", "2021")
    lista=lt.newList(datastructure="ARRAY_LIST")
    for anio in mayor_saldo_favor_anios:
        mayor = None
        for line in lt.iterator(data_structs['model']['data']):
            #esta condicion es porq no quiero q me recorra toda la lista si no solo en las q en el anio es el mismo q estoy iterando
            if line["Año"] == anio:
                if mayor == None:
                    mayor = line
                else:
                    if line["Total saldo a favor"] > mayor["Total saldo a favor"]:
                        mayor = line
                    else: 
                        mayor = mayor
        lt.addLast(lista,mayor)
    return lista
    
def req3_4_5(data_structs,compare_function):
  
    "El total de costos y gastos nómina del subsector económico.:  Sector_economico: Costos y gastos nómina "
    
    years=('2021', '2020', '2019', '2018', '2017', '2016', '2015', '2014', '2013', '2012')

    codes_sub_sector=('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25')

    list_1=lt.newList(datastructure="ARRAY_LIST")
    list_2=lt.newList(datastructure='ARRAY_LIST')
    list_subsector_best_dict=lt.newList(datastructure="ARRAY_LIST")

    for year in years:
        list_by_year=lt.newList(datastructure='ARRAY_LIST')
        list_by_year['key']=year

        list_by_year_best_code=lt.newList(datastructure='ARRAY_LIST')
        list_by_year_best_code['key']=year


        for code_sub in codes_sub_sector:
            list_by_code_sub=lt.newList(datastructure="ARRAY_LIST")
            list_by_code_sub['key']=code_sub

            for element in lt.iterator(data_structs['model']['data']):
                if element['Año']==year and element['Código subsector económico']==code_sub:
                    lt.addFirst(list_by_code_sub,element)

            if list_by_code_sub['size']!=0:

                list_by_code_sub_sort=quk.sort(list_by_code_sub,compare_function)
                lt.addFirst(list_by_year_best_code,lt.firstElement(list_by_code_sub_sort))
                lt.addFirst(list_by_year,list_by_code_sub_sort)
                
        if list_by_year['size']!=0:
            lt.addFirst(list_1,list_by_year)
            best_dict=lt.firstElement(quk.sort(list_by_year_best_code,compare_function))
            lt.addFirst(list_subsector_best_dict,best_dict['Código subsector económico'])
            lt.addFirst(list_2,best_dict)

    list_best_aportation=lt.newList(datastructure='ARRAY_LIST')
    for i in range(0,10):
        for j in list_1['elements'][i]['elements']:
            if j['key']==list_subsector_best_dict['elements'][i]:
                lt.addFirst(list_best_aportation,j)

    return list_2,list_best_aportation

def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    return req3_4_5(data_structs,compare_req3_sub)

def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    return req3_4_5(data_structs,compare_req4_sub)

def req_5(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    return req3_4_5(data_structs,compare_req5_sub)
    
def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass

def compare_req3_sub(data_1,data_2):
    return int(data_1['Total retenciones'])<=int(data_2['Total retenciones'])

def compare_req4_sub(data_1,data_2):
    return int(data_1['Costos y gastos nómina'])>=int(data_2['Costos y gastos nómina'])

def compare_req5_sub(data_1,data_2):
    return int(data_1['Descuentos tributarios'])<=int(data_2['Descuentos tributarios'])

def req_7(data_structs, sample):
    
    '''Función que soluciona el requerimiento 7'''
    #ACa llegan los datos ya sublisteados del anio que es
    
    lista_por_costos_y_gastos = quk.sort(data_structs, cmp_total_costos_y_gastos)
    
    lista_sampleada = lt.subList(lista_por_costos_y_gastos, 1, sample)
    
    lista_sampleada_y_ordenada = quk.sort(lista_sampleada, cmp_impuestos_by_anio_solamente)
    
    return lista_sampleada_y_ordenada

def req_8(data_structs, sample):
    """
    Función que soluciona el requerimiento 8
    """

    subsectores = lt.newList("ARRAY_LIST", cmp_subsectores)
    for line in lt.iterator(data_structs):
        nombre_sub =  line["Nombre subsector económico"] 
        presente = lt.isPresent(subsectores, nombre_sub)
        if  presente == 0:
            lt.addLast(subsectores, [line["Código sector económico"], line["Nombre sector económico"], line["Código subsector económico"], nombre_sub ,  int( line["Total Impuesto a cargo"] ), int ( line["Total ingresos netos"] ) , int ( line["Total costos y gastos"] ) , int ( line["Total saldo a pagar"] ) , int ( line["Total saldo a favor"] )  ])
        else:
            lt.getElement(subsectores, presente)[4] += int ( line["Total Impuesto a cargo"] ) 
            lt.getElement(subsectores, presente)[5] += int ( line["Total ingresos netos"] ) 
            lt.getElement(subsectores, presente)[6] += ( int ( line["Total costos y gastos"] ) )
            lt.getElement(subsectores, presente)[7] += ( int ( line["Total saldo a pagar"] ) )
            lt.getElement(subsectores, presente)[8] += ( int ( line["Total saldo a favor"] ) )
    data_sorteada = quk.sort(data_structs, cmp_impuestos_by_subsector)       
    posiciones = posiciones_dado_un_parametro(data_sorteada, "Código subsector económico")
    actividades_que_mas_aportaron_por_subsector = {}
    posible = True
    for pos in range(len(posiciones)):
        if pos == len(posiciones) - 1:
            posible = False
        if posible == True:
            if sample > posiciones[pos+1] -  posiciones[pos]:
                actividades_que_mas_aportaron_por_subsector[lt.getElement(data_sorteada, pos)[ "Nombre subsector económico"]] = lt.subList(data_sorteada, posiciones[pos], posiciones[pos+1] -  posiciones[pos])
            else:
                actividades_que_mas_aportaron_por_subsector[lt.getElement(data_sorteada, pos)[ "Nombre subsector económico"]] = lt.subList(data_sorteada, posiciones[pos], sample)
    top_n_ordenados = {}
    for sub in lt.iterator(subsectores):
        for n in actividades_que_mas_aportaron_por_subsector:
            if sub[3] == n:  
                top_n_ordenados[n] = actividades_que_mas_aportaron_por_subsector.get(n)
    return subsectores, top_n_ordenados

def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    return quk.sort(data_structs,compar_fun_or_load_data)

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

def posiciones_dado_un_parametro(data_structs, id:str):
    
    '''Esta funcion nos devuelve una lista de posiciones [0, 5, 8, 22] que podemos utilizar para realizar sublistas basados en ellas'''

    posiciones = [0]
    
    primera_vez = True
    
    posicion = 0
    
    for line in lt.iterator(data_structs):
        
        if primera_vez == True:
            
            linea_anterior = line
            primera_vez = False
            
        elif line[id] != linea_anterior[id]:
            
            posiciones += [posicion]
            
        linea_anterior = line
            
        posicion += 1
        
    return posiciones

def sublist_por_anio(data_structs, ao, ax):
    
     '''Esta funcion toma por parametro una estructura de datos, un anio inicial y final y te devuelve una sublista desde ese anio hasta el final'''
     
     posiciones = [0]
    
     primera_vez = True
    
     posicion = 0
    
     for line in lt.iterator(data_structs):
        
        if primera_vez == True:
            
            linea_anterior = line
            primera_vez = False
            
        elif line["Año"] != linea_anterior["Año"]:
            
            posiciones += [posicion]
            
        linea_anterior = line
            
        posicion += 1
        
     anios_posibles = {"2012": posiciones[0], "2013": posiciones[1], "2014": posiciones[2], "2015": posiciones[3], "2016": posiciones[4], "2017": posiciones[5], "2018": posiciones[6], "2019": posiciones[7], "2020": posiciones[8], "2021": posiciones[9], "2022": lt.size(data_structs)-1} 
  
     posicion_inicial = anios_posibles.get(ao)
    
     posfi = int(ax) + 1
   
     posicion_final = anios_posibles.get(str(posfi))
    
     numero_filas = posicion_final - posicion_inicial
    
     lista_de_esos_anios = lt.subList(data_structs, posicion_inicial + 1, numero_filas)
    
     return lista_de_esos_anios

def sublist_anio_especifico(data_structs, anio):
    
     '''Esta funcion toma por parametro una estructura de datos, un anio y te devuelve una sublista desde ese anio'''
         
     primera_vez = True
    
     posicion = 0
    
     for line in lt.iterator(data_structs):
        
        if primera_vez == True:
            
            if line["Año"] == anio:
                
                 pos = posicion
                 
                 primera_vez = False
            
        if primera_vez == False:
            
            if line["Año"] == anio:
                
                pos_final = posicion
            
        posicion += 1

     numero_filas = pos - pos_final
    
     lista_de_esos_anios = lt.subList(data_structs, pos + 1, numero_filas)
    
     return lista_de_esos_anios

def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    return data_1["id"] > data_2["id"]

def cmp_impuestos_by_subsector(impuesto1, impuesto2): 
    """
    Esta funcion sortea por anio, luego por codigo subsector economico de menor a mayor y luego por total impuesto a cargo de mayor a menor
    esto con el fin de luego junto con la funcion de posiciones poder hacer sublistas de lo que ordenemos con esta funcion y tener el top n de elementos de cada subsector
    con mayor impuesto a cargo
    """ 
    if impuesto1["Año"] < impuesto2["Año"]:
        
        retorno = True
        
    elif impuesto1["Año"] == impuesto2["Año"]:
        
        if impuesto1["Código subsector económico"] < impuesto2["Código subsector económico"]:
        
           retorno = True
           
        elif impuesto1["Código subsector económico"] == impuesto2["Código subsector económico"]:

           
           if impuesto1["Total Impuesto a cargo"] > impuesto2["Total Impuesto a cargo"]:
        
                retorno = True
        
           else:
            
                  retorno = False
        
        else:
            
            retorno = False
            
    elif impuesto1["Año"] > impuesto2["Año"]:
        
        retorno = False
        
    return retorno
 
 #CMP FUNCTIONS
 
def cmp_impuestos_by_anio_CAE(impuesto1, impuesto2): 
    """
    Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2, en caso de que sean iguales tenga en cuenta el código de la actividad económica, de lo contrario devuelva falso (False).
    Args:
    impuesto1: información del primer registro de impuestos que incluye el “Año” y el
    “Código actividad económica”
            impuesto2: información del segundo registro de impuestos que incluye el “Año” y el
            “Código actividad económica”
    """ 
    if impuesto1["Año"] < impuesto2["Año"]:
        
        retorno = True
        
    elif impuesto1["Año"] == impuesto2["Año"]:
        
        if impuesto1["Código actividad económica"] < impuesto2["Código actividad económica"]:
        
           retorno = True
        
        else:
            
            retorno = False
            
    elif impuesto1["Año"] > impuesto2["Año"]:
        
        retorno = False
        
    return retorno

def cmp_subsectores(subsector, diccionario):
    
    if subsector > diccionario[1]:
    
        return 1
    
    elif subsector < diccionario[1]:
    
        return -1
    
    elif  subsector == diccionario[1]:
        
        return 0
    
    pass
    
def cmp_total_costos_y_gastos(impuesto1, impuesto2):
    
     if impuesto1["Año"] < impuesto2["Año"]:
        
        retorno = True
        
     elif impuesto1["Año"] == impuesto2["Año"]:
        
         if impuesto1["Total costos y gastos"] < impuesto2["Total costos y gastos"]:
        
           retorno = True
        
         else:
            
            retorno = False
            
     elif impuesto1["Año"] > impuesto2["Año"]:
        
        retorno = False
        
     return retorno
 
def cmp_actividades_economicas_que_mas_aportaron(impuesto1, impuesto2): 
    
    '''Compare function para sortear por anio y dentro de cada anio por retenciones.'''

    
    if impuesto1["Año"] < impuesto2["Año"]:
        
        retorno = True
        
    elif impuesto1["Año"] == impuesto2["Año"]:
        
        if impuesto1["Total retenciones"] < impuesto2["Total retenciones"]:
        
           retorno = True
        
        else:
            
            retorno = False
            
    elif impuesto1["Año"] > impuesto2["Año"]:
        
        retorno = False
        
    return retorno
def cmp_impuestos_by_anio_solamente(impuesto1, impuesto2): 
    """
    Devuelve verdadero (True) si el año de impuesto1 es menor que el de impuesto2, en caso de que sean iguales tenga en cuenta el código de la actividad económica, de lo contrario devuelva falso (False).
    Args:
    impuesto1: información del primer registro de impuestos que incluye el “Año” y el
    “Código actividad económica”
            impuesto2: información del segundo registro de impuestos que incluye el “Año” y el
            “Código actividad económica”
    """ 
    if impuesto1["Año"] < impuesto2["Año"]:
        
        retorno = True
        
    else:
        
        retorno = False
        
    return retorno