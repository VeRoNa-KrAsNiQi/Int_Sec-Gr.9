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
testing = requests.get(url=target_with_payload, headers=header)
    if str(payload) in str(testing.text):
        label4=Label(window,text="Possible XSS Found!",font=("arial",10),fg="indigo",bg="powderblue")
        label4.pack(padx=2,pady=2)
    else:
        label5=Label(window,text="Webpage is safe!",font=("arial",10),fg="indigo",bg="powderblue")
        label5.pack(padx=2,pady=0)
def clearclicked():
    textbox1.delete(0,END)
    textbox1.configure(state="normal")
def submitclicked():
    textbox1.configure(state="normal")
    if validimi():
        skano()
