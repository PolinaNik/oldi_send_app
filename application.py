import os
from tkinter import *

root = Tk()
root.title("SEND OLDI")
root.geometry('800x150')

OPTIONS = ['Магадан', 'Владивосток', 'Якутск', 'Южно-Сахалинск', 'Иркутск', 'Шеньян']
variable = StringVar(root)
variable.set("Отправить OLDI в")

variable2 = StringVar(root)
variable2.set("Отправить OLDI из")

message = StringVar()
message_entry = Entry(textvariable=message)
message_entry.pack(fill=BOTH)

def clear_text():
    message_entry.delete(0, 'end')

def callback1(selection):
    if selection == 'Магадан':
        p = 5
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено в %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable.set("Отправить OLDI в")
    if selection == 'Владивосток':
        p = 3
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено в %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable.set("Отправить OLDI в")
    if selection == 'Якутск':
        p = 1
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено в %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable.set("Отправить OLDI в")
    if selection == 'Южно-Сахалинск':
        p = 8
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено в %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable.set("Отправить OLDI в")
    if selection == 'Иркутск':
        p = 4
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено в %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable.set("Отправить OLDI в")
    if selection == 'Шеньян':
        p = 10
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено в %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()

def callback2(selection):
    if selection == 'Магадан':
        p = 5
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено из %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable2.set("Отправить OLDI из")
    if selection == 'Владивосток':
        p = 3
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено из %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable2.set("Отправить OLDI из")
    if selection == 'Якутск':
        p = 1
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено из %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable2.set("Отправить OLDI из")
    if selection == 'Южно-Сахалинск':
        p = 8
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено из %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable2.set("Отправить OLDI из")
    if selection == 'Иркутск':
        p = 4
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено из %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable2.set("Отправить OLDI из")
    if selection == 'Шеньян':
        p = 10
        os.popen('echo "(%s) to %s" >> /home/polina/pipes' % (message.get(), p))
        l = Label(text="OLDI с текстом:")
        l2 = Label(text="%s" %message.get())
        l3 = Label(text="было отправлено из %s" %selection)
        l.pack()
        l2.pack()
        l3.pack()
        clear_text()
        variable2.set("Отправить OLDI из")
def close():
    root.destroy()
    root.quit()

message_entry.pack(fill=BOTH)

w = OptionMenu(root, variable, *OPTIONS, command=callback1)
w.pack(fill=BOTH)

w2 = OptionMenu(root, variable2, *OPTIONS, command=callback2)
w2.pack(fill=BOTH)

root.protocol('WM_DELETE_WINDOW', close)

root.mainloop()
