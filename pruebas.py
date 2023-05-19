# print ("gracias por elegirme Dani te saluda PYTHON")
#x = input ("Ingrese un texto -->")
#print (x)

#for x in range (10,15):
#    print (x)
#x = 3
'''print("type of", x, "is", type(x))
x = 3.23
print("type of", x, "is", type(x))
x = 3+3j
print("is", x, "a complex number:", isinstance(x, complex))

x = "AcalambraR"
y = x.replace('a', 'e', 2)
z = x.replace('a', 'e')
print(y)
print(z)
palabra_mayus = str.upper(x)
print (palabra_mayus)

texto = "Hola"
lista = list(texto)

print(texto)
print(lista)


#aca ver que no declaro ni tampoco inicializo x lo hizo directo
b = [x for x in range(10)]
print(b)


a = [ x for x in range(0, 101)]
print(a)

b = [ x*2 for x in range(15)]
print(b)


c = [3 * letra for letra in "hola"]
print(c)

palabra = 'Daniel Angel'

c = [letra for letra in palabra]
print(c)

d = [ 10+n for n in [1,2,3,4] ]
print(d)


lista = ["Uno", "Dos", "Tres"]
texto = "".join( lista )

print (lista)
print (texto)

a = [1,2]
b = [3,4]
z = a+b
print(z)

'''
'''
a = ["Hola", "Adios", "Como esta", "Buen día" ]
a.sort()
print(a)

b = [1, 2, 3, 123, 23, 12]
b.sort()
print(b)

# Es posible hacer un orden inverso indicando reverse=True
b.sort(reverse=True)
print(b)
'''
'''
# En este ejemplo la regla es la longitud del elemento
def mi_orden1(e):
  return len(e)

a = ["Hola", "Adios", "Como esta", "Buen día" ]
a.sort(key=mi_orden1)
print("Orden final:", a)

'''

# En este ejemplo se analiza el segundo valor de cada elemento
def mi_orden2(e):
  return e[1]

area = [ ["Argentina", 2.78], ["Brazil", 8.51], ["Mexico", 1.96] ]
area.sort(key=mi_orden2)
print("Orden final:", area)