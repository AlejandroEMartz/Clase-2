# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 14:50:59 2021

@author: Usuario
"""
def buscar_precios(fruta):
    f = open ('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\precios.csv')
    

    
    fruta=str(fruta) #hago string a la fruta
   
    # buscar en el archivo la fruta
    for line in f:
        col = line.split(',') #separo filas en vector 
        
        if fruta in line: # si la fruta está en la fila
            
            precio = col[1]
            #print(precio)
    
            
            #print(precio)
           
            f.close() 
            return precio



preciof = buscar_precios('Naranja') 
print('el precio de la fruta es: ' + preciof)