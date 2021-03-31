﻿"""
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
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def initCatalog():
    """
    Inicializa el catalogo de videos
    """
    return controller.initCatalog()

def printResults(ord_videos): 
    size = lt.size(ord_videos) 
    #if size > sample: 
        #print("Los primeros ", sample, " videos ordenados son:") 
    i=1 
    while i <= size: 
        video = lt.getElement(ord_videos,i) 
        print('Trending_date: ' + video['trending_date'] + ' Title: ' + video['title'] + ' Channel_title: ' + video['channel_title'] + ' publish_time: ' + video['publish_time'] +
                ' views: '+ video['views'] + ' likes: '+ video['likes'] + ' dislikes: '+ video['dislikes']) 
        i+=1

def loadData(catalog):
    """
    Carga los videos en la estructura de datos
    """
    return controller.loadData(catalog)

catalog = None


def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Encontrar los n videos con más likes para el nombre de una categoría específica")
    print("3- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        answer= loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        print('Categorias cargadas: ' + str(lt.size(catalog['categories'])))
        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")


    elif int(inputs[0]) == 2:
        size = int(input("Indique el número de videos que quiere listar: ")) 
        category = input ("Ingrese la categoría que quiere consultar: ")
        if size > lt.size(catalog['videos']):
            print ("el tamaño de muestra solicitado excede la cantidad de datos de videos cargados")
        else:
            result = controller.getVideosLikesByCategory(catalog, category, size) 

        printResults(result)

    else:
        sys.exit(0)
sys.exit(0)
