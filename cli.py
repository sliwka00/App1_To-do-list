import functions

while True:
    user_action = input("Type add, show, edit, complete  or exit: ")
    user_action = user_action.strip()  # usuwa spacje z user_action

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + "\n")

        functions.write_todos(todos)  # wprowadzamy fukcje write_todos żeby ograniczyc powtrzalne części kodu, parametry filepath jest zdefiniowany w funkcji , wiec nie trzeba go powtarzać


    elif user_action.startswith("show"):
        todos = functions.get_todos()

        new_todos = [item.strip("\n") for item in
                     todos]  # LIST COMPREHENSIONS:  tworzy nowa listę w której z elementów ze starej listy usuwa "\n"

        for index, item in enumerate(new_todos):
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"

            functions.write_todos(todos)  # mozna też wskazywać nazwę parametru funkcji np. write_todos(filepath="todos.txt",todos_arg=todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("There is no item with that number")
        continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")
print('BYE!')



