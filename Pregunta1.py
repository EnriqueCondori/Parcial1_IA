# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 16:30:03 2020

@author: WIN
"""
import pandas as pd
import numpy as np
from scipy import stats
import math
# Obtenemos los datos de nustro Cvs
datos = pd.read_csv("datos.csv")
# print(df["nota"])

# A)La media y la desviación estándar y explique qué significa
#  en cada caso mediante python sin uso de librerías
# LA media sin libreria
#Es una valor promedio de nuestro conjunto de datos selecionados
#en este caso las nota promedio de todos los estudiantes selecionados llegan a
# a tener un nota
#
# def mean(numbers):
#     return float(sum(numbers)) / max(len(numbers), 1)
# print("\n Media sin lib:\n%s"%(mean(df["nota"])))


def media(lista):
    suma=0
    for i in range(len(lista)):
        suma=lista[i]+suma
    suma=suma/len(lista)
    return suma
# lista=df["nota"]
def desviacionE(lista):
    x=media(lista)
    v=0
    for i in range(len(lista)):
        v=((lista[i]-x)*(lista[i]-x))+v
    v=v/(len(lista)-1)
    return math.sqrt(v)
print("\n-------- NOTA ---------")
lista=datos["nota"]
print("La nota promedio es:",media(lista))
# En este caso la edad promedio que tiene un estudiante es de:
print("La desviacion estandar de nota es:",desviacionE(lista))
#hay una gran variacion entre los datos de la nota    
print("-------- EDAD ---------")
lista=datos["edad"]    
print("La Edad promedio de un estuante es:",media(lista))
#----------------------------------------------------------------------
# la desciacion estandar de la columna tabla es
# indica las dispersion de los datos con respecto al la media
lista=datos["edad"]
print("La desviacion estandar de edad es:",desviacionE(lista))
#no llega a ver tanta variacion
# ----------------------------------------------------------------------------
# b)La media, la moda, la desviación estándar con el uso de numpy y pandas
# -------------- USO CON PANDA -----------------
print("\n---------------USO DE LIBRERIAS PANDAS-------------------")
print("........... NOTA .................")
media = datos["nota"].mean()
moda = datos["nota"].mode()
des=datos["nota"].std()
#impresiones
print("Media : %s"%(media))
print("Moda : %s"%(moda))
print("Desviavion Standar de Nota S: %s"%(des))
print("........... EDAD ...............")
media = datos["edad"].mean()
moda = datos["edad"].mode()
des=datos["edad"].std()
#impresiones
print("Media : %s"%(media))
print("Moda : %s"%(moda))
print("Desviavion Standar de edad S: %s"%(des))
print("\n---------------USO DE LIBRERIAS NUMPY-------------------")
edad=np.array(datos["edad"])
notas=np.array(datos["nota"])
# print(edad)
# print(notas)
print("........... NOTA .................")
media = np.mean(notas)
#mode = stats.mode(notas)
moda=pd.DataFrame(notas)
des=np.std(notas)
#impresiones
print("Media : ",(media))
print("Moda : ",moda.mode())
print("Desviavion Standar:",(des))
print("........... EDAD ...............")
media = np.mean(edad)
moda=pd.DataFrame(edad)
#mode = stats.mode(edad)
des=np.std(edad)
#impresiones
print("Media : ",(media))
print("Moda : ",(moda.mode()))
print("Desviavion Standar : ",(des))
