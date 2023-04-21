def get_todos(filepath="todos.txt"):  # wprowadzam funkcje bo powtarza sie ta czynność kilkukrotnie i krótszy kod gdy bedzie funkcja.
    """Read a text file and return the list of
     to-do items."""
    with open(filepath,'r') as file_local:  # wprowadzamy do zmiennych dopisek "_local" żeby nie miały takich samych nazw jak w głównym kodzie
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """write the to-do items list in the text file"""
    with open('todos.txt', 'w') as file:
        file.writelines(todos_arg)

