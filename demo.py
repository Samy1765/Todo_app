import FreeSimpleGUI as gui
import time
import os

if not os.path.exists("demo.txt"):
    with open("demo.txt", "w") as f:
        pass

def fileread():
    with open("demo.txt", 'r') as file:
        content = file.readlines()
        return [task.strip() for task in content]

def filewrite(file):
    with open("demo.txt", 'a') as fileq:
        for task in file:
            fileq.write(task + "\n")

gui.theme("BlueMono")
clock=gui.Text('',key='date')
label = gui.Text("To-do")
inp = gui.InputText(tooltip="enter tasks", key="keys")
button = gui.Button("Add")
listbox = gui.Listbox(values=fileread(), key="items", enable_events=True, size=(40, 10))
edit = gui.Button("Edit",size=5)
delete = gui.Button("Complete")
exit=gui.Button("Exit")

window = gui.Window("My To Do Task App", layout=[[clock],[label],[inp, button],[listbox,edit,delete],[exit],],font=('italic', 10))

while True:
    event, values = window.read(timeout=10)
    if event != gui.WIN_CLOSED:
     window["date"].update(value=time.strftime("%b - %d - %Y        %H:%M:%S"))
    match event:

        case 'Add':
            newval = values['keys']
            if not newval:
                gui.popup("Please enter a task")
            else:
                filewrite([newval])

            print("Task Added Successfully.")
            window['items'].update(values=fileread())

        case 'Edit':
          try:
            fg = values["items"][0]
            newval = values["keys"]
            filer = fileread()
            index = filer.index(fg)
            filer[index] = newval

            with open("demo.txt", 'w') as fileq:
                for task in filer:
                    fileq.write(task + "\n")
            window['items'].update(values=filer)

          except IndexError:
              gui.popup("Select An Item First.") 

        case 'Complete':
         try:
            fg = values["items"][0]
            filer = fileread()
            index = filer.index(fg)
            del filer[index]
            with open("demo.txt", 'w') as fileq:
                for task in filer:
                    fileq.write(task + "\n")
                window['items'].update(values=filer)
                window['keys'].update(value='')

         except IndexError:
            gui.popup("Select An Item First.")

        case 'Exit':
            break

        case 'items':
            window["keys"].update(value=values['items'][0])

        case gui.WIN_CLOSED:
            break
window.close()