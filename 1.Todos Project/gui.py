import functions as f
import PySimpleGUI as gui

label = gui.Text("Please enter your text here")
input_box = gui.Input(tooltip="You can type your text here", key="todo")
list_box = gui.Listbox(values=f.get_todos(), key='todos',
                       enable_events=True, size=(45, 20))
add_button = gui.Button("Add")
edit_button = gui.Button("Edit")
exit_button = gui.Button("Exit")
delete_button = gui.Button("Delete")

window = gui.Window('TODO List',
                    layout=[[label],
                            [input_box, add_button],
                            [list_box, edit_button, delete_button],
                            [exit_button]],
                    font=('Times New Roman', 12))

while True:
    event, input_entered = window.read()
    match event:
        case 'todos':
            window['todo'].update(value=input_entered['todos'][0].strip())
        case "Add":
            todos = f.get_todos()
            todo = input_entered["todo"] + '\n'
            todos.append(todo)
            f.write_todos(todos)
            window['todos'].update(values=f.get_todos())
            window['todo'].update(value='')

        case "Edit":

            todos = f.get_todos()
            selected_todo = input_entered["todos"][0]
            new_todo = input_entered['todo']

            item_index = todos.index(selected_todo)
            todos[item_index] = new_todo + '\n'

            f.write_todos(todos)

            window['todos'].update(values=f.get_todos())
            window['todo'].update(value='')

        case "Delete":
            todos = f.get_todos()
            todo_to_delete = input_entered['todos'][0]
            # delete_item_index = todos.index(todo_to_delete)
            # todos.pop(delete_item_index)

            todos.remove(todo_to_delete)

            f.write_todos(todos)
            window['todos'].update(values=f.get_todos())
            window['todo'].update(value='')

        case "Exit":
            break

        case gui.WIN_CLOSED:
            break

window.close()
