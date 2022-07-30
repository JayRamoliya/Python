
from pydoc import pager
import tkinter as tk
from turtle import width
from typing import Text
import PyPDF2
from PIL import Image,ImageTk
from tkinter.filedialog import askopenfile


root=tk.Tk()

canvas=tk.Canvas(root,width=600,height=300)
canvas.grid(columnspan=3,rowspan=3)

#instructions
instructions=tk.Label(root,text='select a pdf file on your computer',font='Raleway')
instructions.grid(columnspan=3,column=0,row=1)

def open_file():
    browse_text.set("loading...")
    file=askopenfile(parent=root,mode="rb",title="choosse a file" ,filetype=[("pdf file","*.pdf")])
    if file:
        read_pdf=PyPDF2.PdfFileReader(file)
        page=read_pdf.getPage(0)
        page_content=page.extractText()
        
        text_box=tk.Text(root,height=10,width=50,padx=15,pady=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center",justify='center')
        text_box.tag_add("center",1.0,'end')
        text_box.grid(column=1,row=3)

        browse_text.set("Browse")


browse_text=tk.StringVar()

# Button
btn=tk.Button(root,textvariable=browse_text,font='Raleway',bg="red",fg="white",command=lambda:open_file())
browse_text.set("Browse")
btn.grid(column=1,row=2)


canvas=tk.Canvas(root,width=600,height=250)
canvas.grid(columnspan=3)

root.mainloop()