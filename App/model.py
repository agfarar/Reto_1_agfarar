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
    
def req_3(data_structs):
    
    """
    Función que soluciona el requerimiento 3
    """
    
    menor_subsector_por_anio = {"2012": [], "2013": [], "2014": [], "2015": [], "2016": [], "2017": [], "2018": [], "2019": [], "2020": [], "2021": []}

    for anio in menor_subsector_por_anio:
        
        subsectores = lt.newList("ARRAY_LIST", cmp_subsectores)
    
        for line in lt.iterator(data_structs):
                
                if line["Año"] == anio:
                    
                    subsectores = lt.newList("ARRAY_LIST", cmp_subsectores)
            
                    nombre_sub =  line["Nombre subsector económico"] 
                
                    presente = lt.isPresent(subsectores, nombre_sub)
                            
                    if  presente == 0:
                                        
                        #en el subindice 3 es la suma de total retenciones, 4 es ingresos netos, 5 costos y gastos, 6 saldoa pagar, 7 saldo a favor
                        lt.addLast(subsectores, [anio, line["Código sector económico"], line["Nombre sector económico"], line["Código subsector económico"], nombre_sub ,  int( line["Total retenciones"]  ), int ( line["Total ingresos netos"] ) , int ( line["Total costos y gastos"] ) , int ( line["Total saldo a pagar"] ) , int ( line["Total saldo a favor"] )  ])
                        
                    else:
                        
                        lt.getElement(subsectores, presente)[5] += int (line["Total retenciones"]  ) 
                        lt.getElement(subsectores, presente)[6] += int ( line["Total ingresos netos"] ) 
                        lt.getElement(subsectores, presente)[7] += ( int ( line["Total costos y gastos"] ) )
                        lt.getElement(subsectores, presente)[8] += ( int ( line["Total saldo a pagar"] ) )
                        lt.getElement(subsectores, presente)[9] += ( int ( line["Total saldo a favor"] ) )
                        
                #Y aca ya tendriamos el dicccionario de cada subsector de ese ano con la suma del total de retenciones
                
                primera_vez = True
                
                for i in lt.iterator(subsectores):
                    
                    if primera_vez == True:
                        
                        subsector_minimo = i #aca guarda el nombre de la llave
                        primera_vez = False
                        
                    else:
                
                            if i[5] <  subsector_minimo[5]:
                                    
                                subsector_minimo = i
                
                menor_subsector_por_anio[anio] = subsector_minimo
        
    #Aca agregamos el anio en primera posicion, luego corrijo esto para q se haga desde arriba y minimicemos mas ciclos...
    
    #ESTO ES PARA FACILITAR LA TABULACION EN VIEW
    menor_subsector_lista = []

    for anio in menor_subsector_por_anio:
        
        menor_subsector_por_anio.get(anio).insert(0, anio)
        menor_subsector_lista += [menor_subsector_por_anio.get(anio)]
        
    return menor_subsector_lista

def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4

    #Primera tabla
    
    #Sumatoria del primero 
    "El total de costos y gastos nómina del subsector económico.:  Sector_economico: Costos y gastos nómina "
    list_subsector_by_year=lt.newList(datastructure="ARRAY_LIST")
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
                    #Aca
                    list_by_code_sub_sort=quk.sort(list_by_code_sub,comare_req4_sub)
                    lt.addFirst(list_by_code,list_by_code_sub_sort)

            if list_by_code['size']!=0:
                lt.addFirst(list_by_year,list_by_code)
        lt.addFirst(list_ord_by_year_and_code,list_by_year)
        
        #Año - codigo- sub_codigo
#bueno aca la idea es organizar el nuevo diccionario  de acuerdo a los requerimientos 
    list_ord_by_year_and_code_sum=lt.newList(datastructure="ARRAY_LIST")
    for year in lt.iterator(list_ord_by_year_and_code):
        list_by_year=lt.newList(datastructure='ARRAY_LIST')
        list_by_year['key']=year['key']
        for key_sup in lt.iterator(year):
            list_by_code=lt.newList(datastructure='ARRAY_LIST')
            list_by_code['key']=key_sup['key']

            for key_inf in lt.iterator(key_sup):#key inferior que tiene  un cojunto de key inferiorres 
                list_by_code_sub=lt.newList(datastructure="ARRAY_LIST")
                list_by_code_sub['key']=key_inf['key']

                diccionario={'Año':year['key'],'Nombre sector económico':None,'Código sector económico':key_sup['key'],'Nombre subsector económico':None,'Código subsector económico':key_inf['key'],'total de costos y gastos nómina del subsector económico':0,'total ingresos netos del subsector económico':0,'total costos y gastos del subsector económico':0,'total saldo por pagar del subsector económico':0}
                   
                for element in lt.iterator(key_inf):
                        
                    diccionario['Nombre sector económico']=element['Nombre sector económico']
                    diccionario['Nombre subsector económico']=element['Nombre subsector económico']
                    diccionario['total de costos y gastos nómina del subsector económico']+=int(element['Costos y gastos nómina'])
                    diccionario['total ingresos netos del subsector económico']+=int(element['Total ingresos netos'])
                    diccionario['total costos y gastos del subsector económico']+=int(element['Total costos y gastos'])
                    diccionario['total saldo por pagar del subsector económico']+=int(element['Total saldo a pagar'])
            lt.addLast(list_by_year,diccionario)

        best_dict=lt.getElement(quk.sort(list_by_year,compare_req4),0)

        dict_best_key_sup_and_inf=[best_dict['Código sector económico'],best_dict['Código subsector económico']]
        lt.addLast(list_subsector_by_year,dict_best_key_sup_and_inf)
        lt.addFirst(list_ord_by_year_and_code_sum,best_dict)
 #arreglar para que no tenga tantas funciones
    list_higher_aportations=lt.newList(datastructure="ARRAY_LIST")
    for k in range(0,10):
        for i in list_ord_by_year_and_code['elements'][::-1]:
            for j in lt.iterator(i):
                if j['key']==list_subsector_by_year['elements'][k][0]:#reemplazar por getElement
                    for l in lt.iterator(j):
                        if l['key']==list_subsector_by_year['elements'][k][1]:
                            lt.addFirst(list_higher_aportations,l['elements'])

                    
    return list_ord_by_year_and_code_sum,list_higher_aportations
    # return list_ord_by_year_and_code_sum
            
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


def req_7(data_structs, ao, ax, sample):
    
    '''Función que soluciona el requerimiento 7'''
    
    #Antes de meterla al sort tengo q hacer una sublista con los elementos de los anios solamente.
    
    posiciones = [0]
    
    #Este for me tira las posiciones en las que se cambia de anio, para yo usarlas para hacer sublistas, aca podriamos llamar a la funcion sublist por anio tal vez.
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
        
    anios_posibles = {"2012": posiciones[0], "2013": posiciones[1], "2014": posiciones[2], "2015": posiciones[3], "2016": posiciones[4], "2017": posiciones[5], "2018": posiciones[6], "2019": posiciones[7], "2020": posiciones[8], "2021": posiciones[9]}

    #Esto me da la posicion correspondiente a cada anio
  
    posicion_inicial = anios_posibles.get(ao)
    
    #Porq como mi mini for me dice cuando cambio de anio en realidad tengo q hacerlo hasta antes de 2015 osea en 2014 + 1 por ejemplo
    posfi = int(ax) + 1
    
    #Aqui hay q poner antes un if en el view para q metan los anios q son porq si no saca error el get .

    posicion_final = anios_posibles.get(str(posfi))
    
    numero_filas = posicion_final - posicion_inicial
    
    lista_ordenada = lt.subList(data_structs, posicion_inicial + 1, numero_filas+1)
    #Aca ya tengo mi sublista desde el anio hasta el otro anio.     
    
    lista_por_costos_y_gastos = quk.sort(lista_ordenada, cmp_total_costos_y_gastos)
    
    #AQUI HAY Q PONER UN IF SI ES MENOR AL SAMPLE.......para q no sqeu error
    lista_sampleada = lt.subList(lista_por_costos_y_gastos, 1, sample)
    
    lista_sampleada_y_ordeanda_por_anio = quk.sort(lista_sampleada, cmp_total_costos_y_gastos)

    return lista_sampleada_y_ordeanda_por_anio


def req_8(data_structs, sample):
    """
    Función que soluciona el requerimiento 8
    """

    subsectores = lt.newList("ARRAY_LIST", cmp_subsectores)
    
    #Recorremos la lista limitada por anios que pasamos desde el controler invocando a la funcion sublist por anio.
    for line in lt.iterator(data_structs):
        
        nombre_sub =  line["Nombre subsector económico"] 
        
        presente = lt.isPresent(subsectores, nombre_sub)
        
        if  presente == 0:
            
            
            #en el subindice 3 es la suma de total retenciones, 4 es ingresos netos, 5 costos y gastos, 6 saldoa pagar, 7 saldo a favor
            lt.addLast(subsectores, [line["Código sector económico"], line["Nombre sector económico"], line["Código subsector económico"], nombre_sub ,  int( line["Total Impuesto a cargo"] ), int ( line["Total ingresos netos"] ) , int ( line["Total costos y gastos"] ) , int ( line["Total saldo a pagar"] ) , int ( line["Total saldo a favor"] )  ])
                        
        else:
            
            lt.getElement(subsectores, presente)[4] += int ( line["Total Impuesto a cargo"] ) 
            lt.getElement(subsectores, presente)[5] += int ( line["Total ingresos netos"] ) 
            lt.getElement(subsectores, presente)[6] += ( int ( line["Total costos y gastos"] ) )
            lt.getElement(subsectores, presente)[7] += ( int ( line["Total saldo a pagar"] ) )
            lt.getElement(subsectores, presente)[8] += ( int ( line["Total saldo a favor"] ) )
            
        #Al final esto nos bota un diccionario con cada subsector y una lista con todas las retencioones ingresos costos y saldos totales.
        
    #ACA ES PARA IMPRIMIR LOS N DATOS POR CADA SUBSECTOR 
    
    data_sorteada = quk.sort(data_structs, cmp_impuestos_by_subsector)
        
    posiciones = posiciones_dado_un_parametro(data_sorteada, "Código subsector económico")

    #Esto sera una lista de un monton de sublistas de dislib
    actividades_que_mas_aportaron_por_subsector = {}
        
    posible = True
    
    for pos in range(len(posiciones)):
        
        #Este condicional es para que no de lista index out of range,. 
        if pos == len(posiciones) - 1:
            
            posible = False

        if posible == True:
        
            if sample > posiciones[pos+1] -  posiciones[pos]:
                
                actividades_que_mas_aportaron_por_subsector[lt.getElement(data_sorteada, pos)[ "Nombre subsector económico"]] = lt.subList(data_sorteada, posiciones[pos], posiciones[pos+1] -  posiciones[pos])
                
                
            else:
        #Aqui crea una llave para cada subsector con el top 3. Saca error si son menos del sample pero no he pdodip solucionarlo
                actividades_que_mas_aportaron_por_subsector[lt.getElement(data_sorteada, pos)[ "Nombre subsector económico"]] = lt.subList(data_sorteada, posiciones[pos], sample)
                
                
    #Esto es para filtrar solamente los subsectores que esten dentro de los subsectores que ya filtramos.
    top_n_ordenados = {}
    
    for sub in lt.iterator(subsectores):
        
        for n in actividades_que_mas_aportaron_por_subsector:
            
            if sub[3] == n:
                
                top_n_ordenados[n] = actividades_que_mas_aportaron_por_subsector.get(n)
                #Esto nos devuelve la lista de dislib qeu esta bajo ese nombre subsector en el dict de topnsubsectores
                
        
    #Y actividades que mas aportaron queda ya listo con cada llave siendo el nombre del subsector 
    # y el valor siendo una sublista de dislib con el N subsectores que mas aportaron
    
    return subsectores, top_n_ordenados


# Funciones utilizadas para comparar elementos dentro de una lista
#Ordenana de mayor a menor
def comare_req4_sub(data_1,data_2):

    return int(data_1['Costos y gastos nómina'])>=int(data_2['Costos y gastos nómina'])
def compare_req4(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    return int(data_1['total de costos y gastos nómina del subsector económico'])>=int(data_2['total de costos y gastos nómina del subsector económico'])

# Funciones de ordenamiento


def sort_criteria(data_1, data_2,id):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    return data_1[id] >=data_2[id]


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    return quk.sort(data_structs,compar_fun_or_load_data)

def cmp_subsectores(subsector, diccionario):
    
    if subsector > diccionario[1]:
    
        return 1
    
    elif subsector < diccionario[1]:
    
        return -1
    
    elif  subsector == diccionario[1]:
        
        return 0

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
def posiciones_dado_un_parametro(data_structs, id:str):
    
    '''Esta funcion nos devuelve una lista de posiciones [0, 5, 8, 22] que podemos utilizar para realizar sublistas basados en ellas'''

    posiciones = [0]
    
    #Este for me tira las posiciones en las que se cambia de anio, para yo usarlas para hacer sublistas.
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
