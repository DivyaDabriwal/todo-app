import functions
import PySimpleGUI as gui

label = gui.Text("Please enter your text here")
input_box = gui.InputText(tooltip="You can type your text here")
add_button = gui.Button(button_text="Add")

window = gui.Window('TODO List', layout=[[label, input_box, add_button]])
window.read()
window.close()
