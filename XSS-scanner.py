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
label1 = Label(window,text="XSS-SCANNER",fg='indigo',bg='powderblue',font=("arial",12,"bold"))
label1.pack(fill=BOTH,pady=20,padx=20)
label2 = Label(window,text="Enter the URL you want to scan:",font=("arial",10),fg="indigo",bg="powderblue")
label2.pack(padx=5,pady=10)
textbox1=Entry(window,font=("arial",12))
textbox1.pack()
def skano():
    header=""
    payloads=open("payloads.txt","r")
    for payload in payloads.readlines():
        target_with_payload = textbox1.get()+str(payload)
