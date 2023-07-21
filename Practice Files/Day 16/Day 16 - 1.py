import PySimpleGUI as gui

label_1 = gui.Text('Enter feet:')
input_1 = gui.InputText()

label_2 = gui.Text('Enter inches:')
input_2 = gui.InputText()

convert_button = gui.Button('Convert')

window = gui.Window("Converter", layout=[[label_1, input_1],
                                         [label_2, input_2],
                                         [convert_button]])
window.read()
window.close()
