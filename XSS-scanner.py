from tkinter import *
import requests
from PIL import ImageTk,Image
window=Tk()
window.geometry("500x500")
window.minsize(500,500)
window.maxsize(500,500)
load=Image.open("images\\a.png")
render=ImageTk.PhotoImage(load)
img=Label(window,image=render)
img.place(x=0,y=0)
window.title("XSS-SCANNER")
data=StringVar()
