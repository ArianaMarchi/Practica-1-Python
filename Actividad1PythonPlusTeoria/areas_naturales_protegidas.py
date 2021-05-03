import json
import csv
import PySimpleGUI as sg

def areas_protegidas():
    layout=[[sg.Text('Se guardaron las 10 provincias con mas áreas naturales protegidas ', size=(20, 2))],
           [sg.Button('Ok', size=(20, 2), key="ok")]]
    
    window = sg.Window('Áreas naturales protegidas', layout)

#----------Archivo csv del dataset----------------------------------
    with open('3_areas-protegidas-cantidad-x-provincia.csv') as csv_file:
        reader = csv.DictReader(csv_file, delimiter = ';')
        lista_de_datos = [row for row in reader]
    lista_de_datos = sorted(lista_de_datos, key=lambda lista_de_datos: int(lista_de_datos['areas_naturales_protegidas_numero']), reverse=True)
    provincias=[]
    for i in range(len(lista_de_datos)):
        provincias.append(lista_de_datos[i]['provincia_desc'])
#------------------------------------------------------------------------
#--------------Abre el archivo json y carga los elementos----------------
    archivo = open('Áreas-protegidas', 'w')
    json.dump('Las 10 provincias con más areas naturales protegidas de argentina', archivo)
    json.dump(provincias[:10], archivo)
    archivo.close()  
#------------------------------------------------------------------------
    while True:
        event, values = window.read()
        if event == 'ok' or event == sg.WINDOW_CLOSED:
           break
    window.close()