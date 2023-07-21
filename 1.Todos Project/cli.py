from functions import get_todos, write_todos

from time import strftime

print(f"It is {strftime('%b %d, %Y %H:%M:%S')}")

while True:
    userInput = input('Type add, show, edit, complete or exit: ').strip()

    if userInput.startswith('add'):
        todo = userInput[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    elif userInput.startswith('edit'):
        try:
            userInputIndex = int(userInput[5:])
            newTodo = input('Enter the new todo: ')

            todos = get_todos()

            if 1 <= userInputIndex <= len(todos):

                todos[userInputIndex - 1] = newTodo + '\n'
                write_todos(todos)
            else:
                print('Out of range')

        except ValueError:
            print('Your command is not valid.')
            continue

    elif userInput.startswith('show'):

        todos = get_todos('todos.txt')

        for index, singleTodo in enumerate(todos):
            formattedTodo = singleTodo.title().strip('\n')
            print(f'{index + 1}. {formattedTodo}')

    elif userInput.startswith('complete'):

        try:
            userInputIndex = int(userInput[9:])

            todos = get_todos()

            if 1 <= userInputIndex <= len(todos):

                completedTodo = todos.pop(userInputIndex - 1).strip('\n')
                print(f'Todo {completedTodo} was removed from the list.')
                write_todos(todos)
            else:
                print('Out of range')

        except IndexError:
            print('Invalid input.')
            continue

    elif userInput.startswith('exit'):
        break
    else:
        print('Invalid command.')
