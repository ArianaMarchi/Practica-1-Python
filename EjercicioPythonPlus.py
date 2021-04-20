import csv

archivo = open("appstore_games.csv", "r")
csvreader = csv.reader(archivo, delimiter = ',')

encabezado = next(csvreader)

lista= []
lista2= []
for linea in csvreader:
    tupla=(linea[4], linea[6])
    lista2.append(tupla)
    if ((linea[7] == '0') and ('ES' in linea[12])):
        lista.append(linea[2])
print('Lista de juegos gratuitos disponibles en idioma español')
for i in range(len(lista)):
    print(lista[i])

lista2.sort(key= lambda lista2: lista2[1])
lista2.reverse()
print('10 maximos')
for i in range(10):
    print(lista2[i][0])