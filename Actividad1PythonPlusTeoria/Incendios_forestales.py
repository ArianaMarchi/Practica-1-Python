import json
import csv
import PySimpleGUI as sg

def incendios():
    layout=[[sg.Text('Se guardaron las 10 provincias con mayor cantidad de incendios forestales en el 2019 ', size=(20, 2))],
           [sg.Button('Ok', size=(20, 2), key="ok")]]
    
    window = sg.Window('Incendio forestales', layout)

#----------Archivo csv del dataset--------------------------------
    with open('incendios-cantidad-causas-provincia.csv') as csv_file:
        reader = csv.DictReader(csv_file, delimiter = ';')
        lista_de_datos = [row for row in reader if row["incendio_anio"]== "2019"]
    lista_de_datos = sorted(lista_de_datos, key=lambda lista_de_datos: int(lista_de_datos['incendio_total_numero']), reverse=True)
    provincias=[]
    for i in range(len(lista_de_datos)):
        provincias.append(lista_de_datos[i]['incendio_provincia'])
#------------------------------------------------------------------------
#--------------Abre el archivo json y carga los elementos----------------
    archivo = open('Incendios forestales 2019', 'w')
    json.dump('Las 10 provincias con mayor cantidad de incendios forestales en el 2019', archivo)
    json.dump(provincias[:10], archivo)
    archivo.close()  
#------------------------------------------------------------------------
    while True:
        event, values = window.read()
        if event == 'ok' or event == sg.WINDOW_CLOSED:
           break
    window.close()