tupla = (1, 2, 3)
print(tupla)
print(tupla[0], tupla[1], tupla[2])





#PARA EL JUEGO DE LOS VOTANTES
'''
lista = ["daniel","pame","valeria","mauri","daniel","pame","pame","pame"]
print(lista)
contar_votos={}
#AGREGAR LOS DATOS DE LA LISTA AL DICCIONARIO Y CONTAR SUS REPETICIONES

for n in lista:
    if n in contar_votos:
        contar_votos[n]+=1
    else:
        contar_votos[n]=1

print('lista detallada de votos',contar_votos)

#for candidatos in contar_votos:
#    print (candidatos, ":",contar_votos[candidatos])


#max = contar_votos.get("daniel")
#max+=1
#print(max)
#print(nombre)
'''
'''
for key,valor in contar_votos.items():
    if max == "":
        max = key,valor
    elif int(max.values()) < valor:
        max = key,valor

print("el canditado con mas valores es :",max)
'''
'''
for candidato in contar_votos:
    if max == 0:
        max = contar_votos.get(candidato)
        nombre = contar_votos.keys(candidato)
'''
'''
#ESTA PARTE ES PARA SACAR EL MAXICMO CANDIDATO CON MAYOR VOTOS
candidato_max =""
valor_max=0

for k,c in contar_votos.items():
    if candidato_max =="" and valor_max == 0:
        candidato_max=k
        valor_max=c
    elif valor_max < c:
        candidato_max=k
        valor_max=c

print("el candidato con mas votos es:",candidato_max)
print("con el numero de votos:",valor_max)
'''

