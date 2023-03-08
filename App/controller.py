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
 """

import config as cf
import model
import time
import csv
csv.field_size_limit(2147483647)

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def new_controller():
     """
     Crea una instancia del modelo
     """
     #TODO: Llamar la función del modelo que crea las estructuras de datos
     control={'model':model.new_data_structs()}
     return control

# Funciones para la carga de datos

def load_data(control:dict):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    raw_data = csv.DictReader(open("Data/DIAN/Salida_agregados_renta_juridicos_AG-small.csv", encoding = "utf-8"), delimiter= ",")
    for line in raw_data:
        model.add_data(control,line)
    return model.data_size(control["model"])
# Funciones de ordenamiento
def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    return model.sort(control["data"])

# Funciones de consulta sobre el catálogo

def get_data(control, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Llamar la función del modelo para obtener un dato
    return model.get_data(control["model"],id)

def req_1(control):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    return model.req_1(control)

def req_2(control):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    return model.req_2(control)

def req_3(control):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    return model.req_3(control)

def req_4(control):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    return model.req_4(control)

def req_5(control):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    return model.req_5(control)

def req_6(control):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(control, ao, ax, sample):
    """
    Retorna el resultado del requerimiento 7, ao anio inicial ax anio final
    """
    
    #Todo se basa en que mi lista me ordene bien todo de menor a mayor
    lista_por_anio = model.sublist_por_anio(control["model"]["data"], ao, ax)
    lista_ordenada = model.req_7(lista_por_anio, sample)
    
    return lista_ordenada

def req_8(control, ao, ax, sample):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    
    #Primero se llama a la funcion sublista por anio, esto para simplificar el orden de crecimiento al trabajar de una vez sobre la lista filtrada
    #con los anios que pidio el usuario
    sublist_por_anio = model.sublist_por_anio(control["model"]["data"], ao, ax)
    
    #Luego de eso ya se llama la funcion 8 pero con la lista reducida
    req_8 = model.req_8(sublist_por_anio, sample)

    return req_8


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
