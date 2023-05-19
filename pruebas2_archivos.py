file = open("noticia.txt") # Guardamos el contenido del archivo en una variable

contenido = file.readlines() # Obtenemos una lista de renglones
#print(contenido)

for line in contenido: 
    print(line) # Mostramos renglón a renglónclear
