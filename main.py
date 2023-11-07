from tkinter import *
from tkinter import  ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


class mainwindow():
    def __init__(self):
        self.root =Tk()
        self.root.resizable(False,False)
        self.root.protocol("WM_DELETE_WINDOW")
        self.root.title("CADASTRO DE ALUNOS EM PYTHON COM TKINTER")
        self.img = ImageTk.PhotoImage(Image.open("background.png"))
        self.panel = Label(self.root,image = self.img)
        self.panel.grid(row=0,column=0)
        self.root.iconbitmap("logo_cadasto.ico")
        self.root.mainloop()
try:
    mainwindow()
except:
    raise Exception ("nao foin possivel rodar esse formulario")