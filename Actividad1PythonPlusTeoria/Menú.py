import PySimpleGUI as sg
from areas_naturales_protegidas import areas_protegidas
from Incendios_forestales import incendios
layout = [[sg.Button('Áreas naturales protegidas en Argentina', size=(30, 2), key= "areas")],
        [sg.Button('Incendios forestales en Argentina', size=(30, 2), key="incendios")],
        [sg.Button('Salir', size=(30, 2))]]

window = sg.Window('Actividad 1 x PythonPlus -TEORIA-',layout)

while True:
    event, values = window.read()
    if event == 'Salir' or event == sg.WINDOW_CLOSED:
        break
    if event == 'areas':
        areas_protegidas()
    if event == 'incendios':
        incendios()
window.close()

