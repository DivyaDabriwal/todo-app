import PySimpleGUI as gui
from zip_extractor import archive_extractor

label_1 = gui.Text('Select archive')
label_2 = gui.Text('Select destination')

archive_input = gui.Input()
destination_input = gui.Input()

archive_button = gui.FileBrowse(key='File')
destination_button = gui.FolderBrowse(key='Folder')

extractor_button = gui.Button('Extractor')

window = gui.Window('Archive Extractor', layout=[[label_1, archive_input, archive_button],
                                                 [label_2, destination_input, destination_button],
                                                 [extractor_button]
                                                 ])

while True:
    event, input_entered = window.read()

    print(event)
    print(input_entered)

    if input_entered:
        archive_extractor(input_entered['File'], input_entered['Folder'])

    if event == gui.WINDOW_CLOSED:
        break

window.close()
