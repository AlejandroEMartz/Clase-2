

def costo_camion(nombre_archivo):
   
  with open (nombre_archivo, "rt") as f:
      header = next(f)
 
      acum = 0
      for line in f:
        row = line.split(',')
        cajones = float(row[1])
        precio = float(row[2])
        precio_final = cajones * precio
        acum += precio_final
       
  
  return acum


nombre_archivo = 'C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\camion.csv'
costo = costo_camion(nombre_archivo)
print(f' costo total:  {costo}')

