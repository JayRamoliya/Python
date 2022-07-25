from tkinter import *
import time

root=Tk()
root.title("Digital Clock")
root.geometry("420x150")
root.resizable(1,1)


text_font=('Boulder', 68, 'bold')
background="#f2e750"
foreground="#363529"
border_width=25

label = Label(root, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def clock():
    time_live=time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200,clock)
clock()
root.mainloop()