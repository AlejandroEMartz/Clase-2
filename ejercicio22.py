with open('C:\\Users\\Usuario\\Desktop\\Python_Unsam\\ejercicios_python\\Data\\camion.csv') as f:
  header = next(f)
  
  acum = 0
  for line in f:
      row = line.split(',')
      cajones = float(row[1])
      precio = float(row[2 ])
      precio_final = cajones * precio
      acum += precio_final
      print(acum)
	
  print ('El costo total es', acum)