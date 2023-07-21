import PySimpleGUI as gui

title_1 = gui.Text("Select files to compare:")
input_text1 = gui.InputText()
choose_button_1 = gui.FilesBrowse("Choose")

title_2 = gui.Text("Select destination folder:")
input_text2 = gui.InputText()
choose_button_2 = gui.FolderBrowse("Choose")

compress_button_3 = gui.Button("Compress")

window = gui.Window(title="File Zipper", layout=[[title_1, input_text1, choose_button_1],
                                                 [title_2, input_text2, choose_button_2],
                                                 [compress_button_3]])
window.read()
window.close()
