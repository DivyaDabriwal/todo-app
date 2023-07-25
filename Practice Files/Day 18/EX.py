import functions as f
import PySimpleGUI as gui
import time

gui.theme('DarkBlue6')

clock = gui.Text('', key='clock')
label = gui.Text("Please enter your text here")
input_box = gui.Input(tooltip="You can type your text here", key="todo",)
list_box = gui.Listbox(values=f.get_todos(), key='todos',
                       enable_events=True, size=(45, 20))

add_button = gui.Button(key="Add", image_source='add.png', size=2, tooltip='Add')
edit_button = gui.Button("Edit")
exit_button = gui.Button("Exit")
delete_button = gui.Button("Delete")

# message = gui.Multiline(key='message')

window = gui.Window('TODO List',
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box, edit_button, delete_button],
                            [exit_button]],
                    font=('Times New Roman', 12))

while True:
    event, input_entered = window.read(timeout=200)
    window['clock'].update(value=time.strftime('%b %d %Y %H:%M:%S'))
    match event:
        case 'todos':
            window['todo'].update(value=input_entered['todos'][0].strip())
        case "Add":
            if input_entered["todo"]:
                todos = f.get_todos()
                todo = input_entered["todo"] + '\n'
                todos.append(todo)
                f.write_todos(todos)
                window['todos'].update(values=f.get_todos())
                window['todo'].update(value='')
            else:
                gui.popup('Please type an input to Add')

        case "Edit":
            try:
                todos = f.get_todos()
                selected_todo = input_entered["todos"][0]
                new_todo = input_entered['todo']

                item_index = todos.index(selected_todo)
                todos[item_index] = new_todo + '\n'

                f.write_todos(todos)

                window['todos'].update(values=f.get_todos())
                window['todo'].update(value='')
            except IndexError:
                gui.popup('Please select an input to Edit')

        case "Delete":
            try:
                todos = f.get_todos()
                todo_to_delete = input_entered['todos'][0]
                # delete_item_index = todos.index(todo_to_delete)
                # todos.pop(delete_item_index)

                todos.remove(todo_to_delete)

                f.write_todos(todos)
                window['todos'].update(values=f.get_todos())
                window['todo'].update(value='')
            except IndexError:
                gui.popup(custom_text='Please select an input to Delete')

        case "Exit":
            break

        case gui.WIN_CLOSED:
            break

window.close()
