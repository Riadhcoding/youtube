from tkinter import *
from pytube import YouTube
root = Tk ()
root.geometry("400x350")
root.title("Youtube video downloader")
def download():
    try:
        myVar.set("Downloading..")
        root.update()
        YouTube(link.get()).streams.first().download()
        link.set("video downloaded successfully")
    except EXCEPTION as e :
        myVar.set ("mistake")
        root.update()
        link.set("Entre correct link")





Label(root, text = "welcome to youtube \n Downloader", font = "Consolas 15 bold").pack()
myVar= StringVar()
myVar.set("Entre the link below")
Entry(root , textvariable=myVar, width=40).pack(pady=10)
link = StringVar()
Entry(root,textvariable=link , width=40).pack(pady=10)
Button(root,text="download video ",command=download).pack()

root.mainloop()