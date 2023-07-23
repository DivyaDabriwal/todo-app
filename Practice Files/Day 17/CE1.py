import PySimpleGUI as gui

feet_label = gui.Text('Enter feet:')
inches_label = gui.Text('Enter inches:')
feet_input = gui.Input(key='feet')
inches_input = gui.Input(key='inches')
convert_button = gui.Button('Convert')
result = gui.Text(key='result')

window = gui.Window('Convertor', layout=[[feet_label,feet_input], [inches_label, inches_input], [convert_button, result]])

while True:
    event, input_entered = window.read()

    feet = input_entered['feet']
    inches = input_entered['inches']

    if feet and inches:
        calculation = int(feet) * 0.3048 + int(inches) * 0.0254
        window['result'].update(value=f'{calculation} m')

    if event == gui.WINDOW_CLOSED:
        break

window.close()
