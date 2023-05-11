import functions
import PySimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo", key="todo")
button=sg.Button("Add")

window=sg.Window("My To-do App",
                 layout=[[label],[input_box],[button]],
                 font=('Helvetica',20))

while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values["todo"]+'\n' # po kliknieciu add tworzy sie slownik gdzie kluczem jest todo a wartością wprowadzona dana
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED: # co się stanie po zamknięciu okna gui
            break
window.close()




