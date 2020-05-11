from tkinter import *
import os

OPTIONS = [
"Jan",
"Feb",
"Mar"
] #etc

master = Tk()

def callback(selection):
    print(selection)
    l = Label(text="%s" %selection, )
    l.pack()

variable = StringVar(master)
variable.set("Отправить из")

w = OptionMenu(master, variable, *OPTIONS, command=callback)
w.pack()

def ok():
    print ("value is:" + variable.get())


button = Button(master, text="OK", command=ok)
button.pack()

mainloop()