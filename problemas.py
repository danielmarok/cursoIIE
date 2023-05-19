#n = int(input())
'''
n = input()
n = int(n)
contador = 0

while n != 1:
    if n % 2 == 0:
        n = n / 2
        contador += 1
    else:
            n = n * 3 + 1
            contador += 1

            
print (contador)
PROBLEMA DE LOTHAR FUNKO
'''

'''
palabra = str (input())
letra = str (input())
#tamano_pal = palabra.len()

while palabra != "":
    if letra in palabra:
        palabra = palabra.replace(letra,"")
    else:
            letra = str (input())

else:
    print("la palabra esta vacia:",palabra)

'''
'''
#JUEGO DEL AHORCADO
palabra = str (input())
palabra=palabra.upper()
n_permitidos = int (input ())
n_permitidos+=1
intentos = 0
#letra =str(input())

while n_permitidos != 0 and palabra != "":
    letra = str(input())
    letra = letra.upper()
    if letra not in palabra:
        n_permitidos-=1
#        letra=str(input())
        intentos+=1
    else:
        palabra=palabra.replace(letra,"")
        intentos+=1
        n_permitidos=n_permitidos
#        letra=str(input())


if n_permitidos == 0:
    print(0)
elif palabra=="":
        print(intentos)

funko en hackerrank
'''

#JUEGO DE LOS VOTANTES

votos_totales=int(input())
candidatos=[]

for n in range (votos_totales):
    candidato = str(input())
    candidatos.append(candidato)


print("TODOS LOS CANDIDATOS",candidatos)

contar_votos ={}

for el_candidato in candidatos:
    if  el_candidato in contar_votos:
        contar_votos[el_candidato]+=1
    else:
        contar_votos[el_candidato]=1

print("LISTA DETALLADA DE LOS CANDIDATOS MAS VOTOS",contar_votos)

candidato_max=""
voto_max=0

for k,c in contar_votos.items():
    if candidato_max =="" and voto_max == 0:
        candidato_max=k
        voto_max=c
    elif voto_max < c:
        candidato_max=k
        voto_max=c

print("el candidato con mas votos es:",candidato_max)
print("con el numero de votos:",voto_max)

