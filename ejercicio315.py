# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 12:09:59 2021

@author: Usuario
"""
#Ejercicio 3.15 tabla_informe.py

import csv

def buscar_precios(fruta):
    precio_fruta = 0.0
    with open('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\precios.csv', 'rt') as f:
        for line in f:
            fila = line.split(',')
            if fila[0] == fruta:
                precio_fruta = float(fila[1])
   
    return precio_fruta
    
    




def costo_camion(nombre_archivo1):
    '''Computa el precio total del camion (cajones * precio) de un archivo'''
    camion = []
    
    costo_total = 0
    with open(nombre_archivo1, 'rt') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
                                     #No se porque usando enumerate() me tira error
                                    #error enumerate: TypeError: zip argument #2 must support iteration
        for row in rows :
            lote = dict(zip(encabezado, row))
            try:
                cajones = int(lote['cajones'])
                precio = float(lote['precio'])
                costo_total += cajones * precio
                
                camion.append(lote)
                 
            except ValueError:
                print(f'Fila {row}: No pude interpretar: {rows}')
            #lote[row[0]]= (int(row[1]), float(row[2]))
            #cajones = float(row[1])
            #precio = float(row[2])
            
            #precio_final = cajones * precio
           # acum += precio_final
     
    
    
    return costo_total

def leer_camion(nombre_archivo1):
    
    camion = []
    #cajon = {}
    #acum = 0
    with open(nombre_archivo1, 'rt') as f:
        rows = csv.reader(f)
        encabezado = next(rows)
        
        for row in rows:
            lote = dict(zip(encabezado, row))
            #lote[row[0]]= (int(row[1]), float(row[2]))
            #cajones = float(row[1])
            #precio = float(row[2])
           # precio_final = cajones * precio
            #acum += precio_final
     
            
            
            camion.append(lote)
    
    
    
    
    
    return camion


#nombre_archivo = 'C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\camion.csv'
#informe = leer_camion(nombre_archivo)
#print(f' informe:  {informe}')


def leer_precios(nombre_archivo2):     
  
#Computa lista de precios de frutas en el mercado 
    with open(nombre_archivo2) as f:
        diccio = {}
        filas = csv.reader(f)
        #diccio = [{fila[0]: fila[1]} for fila in filas if len(fila) == 2]
        vendido = 0  
        for fila in filas: 
           
 
            if len(fila) == 2 :
            
        
                diccio[fila[0]] = float(fila[1])
               
    return diccio


#nombre_archivo = 'C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\precios.csv'
#print(leer_precios(nombre_archivo))

costo = costo_camion('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\fecha_camion.csv')
print('EL COSTO ES: ')
print(costo)


'''lee la lista de productos que transporta el camion / cajones / precios'''
camion = leer_camion('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\fecha_camion.csv')    
print('Los ELEMENTOS DEL CAMION SON')
print(camion)

'''lee lista de precios de venta'''
precios = leer_precios('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\precios.csv')
print('\nFUNCION LEER_PRECIOS.PY \nLISTA PRECIOS:')
print(precios)

recaudacion = 0

for fruta in camion:
    recaudacion += buscar_precios(fruta['nombre']) * int(fruta['cajones'])
    
print('RECAUDACION:')  
print(recaudacion)

diferencia = recaudacion - costo
print('GANACIAS NETAS:')
print(diferencia)

    
def hacer_informe(camion,precio):
    
    cambio=0.0
    informe=[]
    for fruta in camion:
        
            cambio = float(precio[fruta['nombre']]) - float( fruta['precio'])
            Nombre = fruta['nombre']
            Cajones = fruta['cajones']
            Precio = fruta['precio']
            tupla = (Nombre, Cajones, Precio, cambio)
            informe.append(tupla)
    return informe
print("INFORME:")

informe = (hacer_informe(camion, precios))
 
headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')


print('%10s %10s %10s %10s' % headers)
print('---------- ---------- ---------- ----------')
for nombre, cajones, precio, cambio in informe:
   
     print(f'{nombre:>10s} {cajones:>10s} {precio:>10.2s} {cambio:>10.2f}')
     
    
    

