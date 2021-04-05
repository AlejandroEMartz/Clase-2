# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 10:51:09 2021

@author: Usuario
"""

import gzip
with gzip.open('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\camion.csv.gz', 'rt') as f:
    for line in f:
        print(line, end = '')
        
        