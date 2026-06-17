# convertir_temperatura.py
sep = "=" *28
print ("< Conversor de temperatura >")
print (sep)
celsius = float(input("Ingrese la temperatura en °C: "))
Fahrenheit = celsius * 9/5 + 32
print (sep)
print ("< Resultados >")
print ("Conversion: ", celsius, "°C equivalen a ", Fahrenheit, "°F")
