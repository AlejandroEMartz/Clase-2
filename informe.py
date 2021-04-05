# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 14:40:56 2021

@author: Usuario
"""

import csv

def leer_camion(nombre_archivo):
    
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []
    with open(nombre_archivo, 'rt') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        
        for row in rows:
            
            
            lote = (row[0], int(row[1]), float(row[2]))
            camion.append(lote)
           
            
    return camion

nombre_archivo = 'C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\camion.csv'
informe = leer_camion(nombre_archivo)
print(f' informe:  {informe}')