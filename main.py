import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import showerror

name=""
def save(name):
    users = open("users.txt", "a")
    users.write(name)
    users.close()
def delete():
    users=open("users.txt")
    lines=users.readlines()
    while lines:
        del(lines[0])
    users.close()
    y = open("users.txt", "w")
    y.writelines(lines)
    y.close()
def checkTxt():
    filesize = os.path.getsize("users.txt")
    if filesize==0:
        return False
    else:
        return True
def getQuestions():
    global name
    name = nameInput.get()
    delete()
    save(name)
    if checkTxt():
        screen.destroy()
        import quiz
        quiz.screen2.mainloop()
    else:
        showerror(title="ERROR",message="ENTER YOUR NAME PLEASE")

screen=Tk()
screen.title("MENU")
canvas=Canvas(screen,width=800,height=400)
image=ImageTk.PhotoImage(Image.open("Images/bg.jpg"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
screen.resizable(False,False)
icon=PhotoImage(file="Images/icon2.png")
screen.iconphoto(False,icon)
screen.configure(bg='black')

welcomeLabel=Label(text="*** WELCOME MY QUIZ ***",bg="black",fg="aqua",font=('Showcard Gothic',20,'bold'))
welcomeLabel.place(relx = 0.28,rely = 0.03,anchor ='nw')

nameLabel=Label(text="Name: ",bg="black",fg="yellow",font=('Showcard Gothic',20,'bold'))
nameLabel.place(relx = 0.38,rely = 0.23,anchor ='ne')

nameInput=Entry(width=25,fg="black",font="bold")
nameInput.place(relx = 0.74,rely = 0.25,anchor ='ne')

start=Button(text="START",bg="red",font=('Showcard Gothic',24,'bold'),width=15,height=3,command=getQuestions)
start.place(relx = 0.28,rely = 0.5,anchor ='nw')
screen.mainloop()