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


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos



def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos. Adicionalmente crea una lista vacia para guardar el título, el canal, 
    fecha de tendencia, pais, vistas, me gusta, no me gusta. Retorna el catalogo inicializado.
    title, cannel_title, trending_date, country, views, likes, dislikes
    """
    catalog = {'videos': None,
               'channels': None,
               'categories':None,
               'categoriesId':None,
               'countries':None,
               'tags': None}

    catalog['videos'] = lt.newList()

    catalog['channels'] = lt.newList('ARRAY_LIST',
                                    cmpfunction = comparechannels)
    catalog['countries'] = lt.newList('ARRAY_LIST',
                                cmpfunction = comparecountries)
    catalog['tags'] = lt.newList('ARRAY_LIST',
                                cmpfunction=comparetags)
    catalog['categories'] = lt.newList('ARRAY_LIST',
                                cmpfunction=comparecategories)

    catalog['categoriesId'] = mp.newMap(37,
                                maptype='PROBING',
                                loadfactor=0.5,
                                comparefunction=compareCategoryIds)

    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    if video['category_id'] == "":
        return

    lt.addLast(catalog['videos'], video)
    channel = video['channel_title']
    lt.addLast(catalog['channels'], channel)
    country = video['country']
    lt.addLast(catalog['countries'], country)

    #mp.put(catalog['categoriesId'], video['category_id'], video)
    tags = video['tags'].split("|")
    for tag in tags:
        lt.addLast(catalog['tags'], tag)


    categoryIds = catalog['categoriesId']
    if (video['category_id'] == ''):
        return
    categoryId = int(video['category_id'])

    existcategory = mp.contains(categoryIds, categoryId)
    if existcategory:
        entry = mp.get(categoryIds, categoryId)
        category = me.getValue(entry)
    else:
        category = newCategoryId(categoryId)
        mp.put(categoryIds, categoryId, category)
    lt.addLast(category, video)

def newCategoryId(categoryId):

    #entry = {'categoryId': "", "videos": None}
    #entry['categoryId'] = categoryId
    
    entry = lt.newList('ARRAY_LIST')
    #lt.addLast()
    return entry

# Funciones para creacion de datos
def addCategory(catalog, category):
    """
    Adiciona una categoria a la lista de categorías
    """
    c = newCategory(category['id'], category['name'])
    lt.addLast(catalog['categories'], c)


# Funciones de consulta

def getVideosLikesByCategory(catalog,category,n):

    index_category = 1

    while category.lower() not in lt.getElement(catalog["categories"], index_category)["name"].lower() :
        index_category += 1

    id_category = lt.getElement(catalog["categories"],index_category)["id"]

    category = mp.get(catalog['categoriesId'], int(id_category))

    if category:
        result = me.getValue(category)
        result = mg.sort(result, compareVideosLikes)
        result = lt.subList(result, 1, n)
    else:
        result = None

    return result

def newCategory(id, name):
    """
    Esta estructura almancena las categorías utilizados para marcar videos.
    """
    category = {'name': '', 'id': ''}
    category['name'] = name
    category['id'] = id
    return category

# Funciones utilizadas para comparar elementos dentro de una lista


def compareVideosLikes(video1, video2):
    if(int(video1['likes']) > int(video2['likes'])):
        return True
    return False


def comparechannels(channelname, channel2):
    if (channelname.lower() in channel2['name'].lower()):
        return 0
    return -1

def comparecountries(countryname, country2):
    if (countryname.lower() in country2['name'].lower()):
        return 0
    return -1

def comparetags(tagname, tag2):
    if (tagname.lower() in tag2['name'].lower()):
        return 0
    return -1

def comparecategories(categoryname, category):
    return (categoryname == category['name'])

def compareCategoryIds(id1, entry):
    """
    Compara los ids de dos categorías
    """

    identry = me.getKey(entry)
    if (int(id1) == int(identry)):
        return 0
    elif (int(id1) > int(identry)):
        return 1
    else:
        return -1

# Funciones de ordenamiento
