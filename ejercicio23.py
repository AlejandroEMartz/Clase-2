# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 01:31:17 2021

@author: Usuario
"""

f = open ('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\precios.csv')


fruta=input("Escriba la fruta que para averiguar su precio: ")
fruta=str(fruta) #hago string a la fruta
   
    # buscar en el archivo la fruta
for line in f:
    col = line.split(',') #separo filas en vector 
       
    if fruta in line: # si la fruta está en la fila
            
        precio = col[1]
            #print(precio)
    
            
            #print(precio)
print('El precio de la fruta es '+ precio) 
f.close() 






        