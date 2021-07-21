from tkinter import Label,Tk
import time

root = Tk()
root.title('Digital Clock')
root.geometry('630x110')
root.resizable(True,True)

label =Label(root,font = ('calibri',40,'bold'),bg = 'black',fg = 'white',bd = 25)
label1 = Label(root,text='DATE / TIME:',font = ('calibri',15,'bold'),bg='black',fg='white').place(x=250 ,y=10)
label.grid(row=0,column=1)


def digital_clock():
    live_time = time.strftime('%a %d/%m/%y %r')
    label.config(text = live_time)
    label.after(1000,digital_clock)

digital_clock()
root.mainloop()