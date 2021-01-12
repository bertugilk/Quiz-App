from tkinter import *
from PIL import ImageTk,Image
import Database
import mysql.connector

myDB=mysql.connector.connect(
    user='root',
    password='1234',
    host='127.0.0.1',
    database='quizapp'
)
cursor = myDB.cursor()

def writeScore():
    Database.getScore()
    Database.getName()
    scoreLabel['text']=Database.name+" SCORE IS: "+Database.score+" /100"
def homeFunction():
    screen3.destroy()
    import main
    main.screen.mainloop()

screen3 = Tk()
screen3.title("QUIZ")
canvas = Canvas(screen3, width=700, height=450,bg='deepskyblue')
image = ImageTk.PhotoImage(Image.open("Images/ok.png"))
canvas.create_image(270, 100, anchor=NW, image=image)
canvas.pack()
screen3.resizable(False, False)
icon = PhotoImage(file="Images/icon2.png")
screen3.iconphoto(False, icon)
screen3.configure(bg='black')

congLabel = Label(text="Congratulations",bg="deepskyblue", fg="red", font=('Showcard Gothic', 22, 'bold'))
congLabel.place(relx=0.72, rely=0.06, anchor='ne')

scoreLabel = Label(bg="deepskyblue", fg="black", font=('Showcard Gothic', 20, 'bold'),wraplengt=350)
scoreLabel.place(relx=0.7, rely=0.65, anchor='ne')

home = Button(text="GO TO HOME", bg="deeppink", fg="black", font=('Showcard Gothic', 14, 'bold'),width=20, height=2,command=homeFunction)
home.place(relx=0.28, rely=0.83, anchor='nw')

writeScore()

screen3.mainloop()