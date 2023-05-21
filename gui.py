import functions
import PySimpleGUI as sg
import time

sg.theme("Black") #gotowe motywy z kolorystyka do podejrzenia w internecie

clock=sg.Text('',key='clock')
label=sg.Text("Type in a to-do")
input_box=sg.InputText(tooltip="Enter todo", key="todo")
button=sg.Button("Add",size=10)
list_box=sg.Listbox(values=functions.get_todos(), size=(45, 10),
                    key='todos', enable_events=True)
edit_button=sg.Button("Edit")
complete_button=sg.Button("Complete")
exit_button=sg.Button("Exit")

window=sg.Window("My To-do App",
                 layout=[[clock],
                         [label],
                         [input_box,button],
                         [list_box, edit_button,complete_button],
                         [exit_button]],
                 font=('Helvetica',20))

while True:
    event,values=window.read(timeout=200)  #timeout=200 powoduje że pętla jest uruchomiana co 200 milisekund (odświeża okno)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S")) #przy starcie aktualizujemy clock

    match event:
        case "Add":
            todos=functions.get_todos()
            new_todo=values["todo"]+'\n' # po kliknieciu add tworzy sie slownik gdzie kluczem jest todo a wartością wprowadzona dana
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos) #aktualizuje od razu liste o nowo dodany 'todo'
        case "Edit":    #cały edit napisany bez spoglądania w kurs ale wygląda na to że działa
            try:
                todos = functions.get_todos() #own
                todo_number=list_box.get_indexes()[0]  #zwraca numer klikniętego 'todo'
                todos[todo_number]=values['todo']+"\n"
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup('please select item first',font=('Helvetica',20))   #gdy błąd wyskoczy popup
        case 'todos':
            window['todo'].update(value=values['todos'][0])   #dzięki temu po kliknieciu na zadanie do edycji pojawia(odświeża) się w inputboxie
        case 'Complete':
            try:
                todos = functions.get_todos()
                todo_number = list_box.get_indexes()[0]
                todos.pop(todo_number)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='') #po usunięciu pozycji z listy "czyścimy" inputbox, żeby był pusty
            except IndexError:
                sg.popup('please select item first', font=('Helvetica', 20))
        case 'Exit':
            break
        case sg.WIN_CLOSED: # co się stanie po zamknięciu okna gui
            break
window.close()




