import PySimpleGUI as gui
import Day17 as archiver

title_1 = gui.Text("Select files to compare:")
input_text1 = gui.InputText()
choose_button_1 = gui.FilesBrowse("Choose", key='files')

title_2 = gui.Text("Select destination folder:")
input_text2 = gui.InputText()
choose_button_2 = gui.FolderBrowse("Choose", key='folder')

compress_button_3 = gui.Button("Compress")
message = gui.Text(key='message')

window = gui.Window(title="File Zipper", layout=[[title_1, input_text1, choose_button_1],
                                                 [title_2, input_text2, choose_button_2],
                                                 [compress_button_3, message]])
# while True:
#     event, values = window.read()
#     files = values['files'].split(';')
#     destination_folder = values['folder']
#     archiver.archive_creator(destination_folder, files)
#     window['message'].update(value='Compression Successful')
#
#     if event == gui.WIN_CLOSED:
#         break

while True:
    event, values = window.read()
    if event == gui.WINDOW_CLOSED:
        break

    print(event, values)

    if values["files"]:
        filepaths = values["files"].split(";")
        folder = values["folder"]
        archiver.archive_creator(folder, filepaths)
        window["message"].update(value="Compression completed!")
    else:
        window["message"].update(value="No files selected!")

window.close()
