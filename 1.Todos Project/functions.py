FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ Gets the content from the file """
    with open(filepath, 'r') as file_get:
        todos_from_file = file_get.readlines()

    return todos_from_file


def write_todos(new_todos, filepath=FILEPATH):
    """ Writes the context to the file """
    with open(filepath, 'w') as file_write:
        file_write.writelines(new_todos)
