# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:45:43 2021

@author: Usuario
"""

import csv
#def leer_fila(row):
 #   if fila[]
        
        
def leer_precios(nombre_archivo,):     
  
   
    with open(nombre_archivo) as f:
        diccio = {}
        filas = csv.reader(f)
        #diccio = [{fila[0]: fila[1]} for fila in filas if len(fila) == 2]
          
        for fila in filas: 
           
 
            if len(fila) == 2 :
            
        
                diccio[fila[0]] = float(fila[1])
        
   
    return diccio



nombre_archivo = 'C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\precios.csv'
print(leer_precios(nombre_archivo))


