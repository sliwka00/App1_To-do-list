import functions
import PySimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo", key="todo")
button=sg.Button("Add")
list_box=sg.Listbox(values=functions.get_todos(), size=(45, 10),
                    key='todos', enable_events=True)
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")

window=sg.Window("My To-do App",
                 layout=[[label],
                         [input_box,button],
                         [list_box, edit_button,complete_button],
                         [exit_button]],
                 font=('Helvetica',20))

while True:
    event,values=window.read()
    print(event)     # po kliknięciu w Button event to jego nazwa, dzięki temu można zrobić poniżej case , reagujace na klikniecie
    print(values)
    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values["todo"]+'\n' # po kliknieciu add tworzy sie slownik gdzie kluczem jest todo a wartością wprowadzona dana
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos) #aktualizuje od razu liste o nowo dodany 'todo'
        case "Edit":    #cały edit napisany bez spoglądania w kurs ale wygląda na to że działa
            todos = functions.get_todos() #own
            todo_number=list_box.get_indexes()[0]  #zwraca numer klikniętego 'todo'
            todos[todo_number]=values['todo']+"\n"
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])   #dzięki temu po kliknieciu na zadanie do edycji pojawia(odświeża) się w inputboxie
        case 'Complete':
            todos = functions.get_todos()
            todo_number = list_box.get_indexes()[0]
            todos.pop(todo_number)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='') #po usunięciu pozycji z listy "czyścimy" inputbox, żeby był pusty
        case 'Exit':
            break
        case sg.WIN_CLOSED: # co się stanie po zamknięciu okna gui
            break
window.close()




