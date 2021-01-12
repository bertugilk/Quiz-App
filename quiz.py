from tkinter import *
from PIL import ImageTk,Image
import Database
import mysql.connector
import pygame

pygame.init()
pygame.mixer.music.load("Sounds/countdown.mp3")
pygame.mixer.music.play()
read = open("users.txt", "r")
user = read.readlines()
read.close()
name=user[0]

myDB=mysql.connector.connect(
    user='root',
    password='1234',
    host='127.0.0.1',
    database='quizapp'
)
cursor = myDB.cursor()

screen2 = Tk()
screen2.title("QUIZ")
canvas = Canvas(screen2, width=900, height=600)
image = ImageTk.PhotoImage(Image.open("Images/bg3.jpg"))
canvas.create_image(0, 0, anchor=NW, image=image)
canvas.pack()
screen2.resizable(False, False)
icon = PhotoImage(file="Images/icon2.png")
screen2.iconphoto(False, icon)
screen2.configure(bg='black')

canvas2 = Canvas(screen2, width=600, height=280,bg="white")
canvas2.place(relx=0.84, rely=0.35, anchor='ne')

r=IntVar()
A_radio=Radiobutton(canvas2, text="A-",variable=r,value=1,bg="white",fg="black",font=('Segoe UI', 16, 'bold'))
A_radio.place(rely=0.5, anchor=W)
B_radio=Radiobutton(canvas2, text="B-",variable=r,value=2,bg="white",fg="black",font=('Segoe UI', 16, 'bold'))
B_radio.place(rely=0.62, anchor=W)
C_radio=Radiobutton(canvas2, text="C-",variable=r,value=3,bg="white",fg="black",font=('Segoe UI', 16, 'bold'))
C_radio.place(rely=0.74, anchor=W)
D_radio=Radiobutton(canvas2, text="D-",variable=r,value=4,bg="white",fg="black",font=('Segoe UI', 16, 'bold'))
D_radio.place(rely=0.86, anchor=W)

correct = 0
wrong = 0
score = 0
SquareColor="yellow"
question_num=1
rectangles = [None for _ in range(5)]
x1 = 0
x2 = 50
k = 0.040
num = 0
colour = ""
counter=1

for i in range(0, 10):
    x1 += 80
    x2 += 80
    k += 0.089
    num += 1
    canvas.create_rectangle(x1, 20, x2, 70, outline="#FFFFFF", fill="")
    number = Label(text=("{0}".format(num)), bg="#696969",fg="black", font=('Showcard Gothic', 20, 'bold'))
    number.place(relx=k, rely=0.045, anchor='ne')

def save():
    global question_num,r,correct,wrong,score,colour,counter
    if check(question_num):
        correct+=1
        colour="green"
    else:
        wrong+=1
        colour="red"
    question_num += 1
    counter+=1
    if question_num > 10:
        question_num = 10
        save["state"] = "disabled"
    questionNumberLabel['text'] = "Q.{0}".format(question_num)
    Database.getQuestions(question_num)
    questionLabel["text"] = (Database.question)
    Database.getA(question_num)
    Database.getB(question_num)
    Database.getC(question_num)
    Database.getD(question_num)
    A_radio["text"] = Database.A
    B_radio["text"] = Database.B
    C_radio["text"] = Database.C
    D_radio["text"] = Database.D
    score = correct * 10
    if score<=0:
        score=0
    canvas.itemconfig(counter, fill=colour)

def finish():
    global name,correct, wrong, score
    Database.insert(name,correct, wrong, score)
    screen2.destroy()
    pygame.mixer.music.stop()
    import result
    result.screen3.mainloop()

questionNumberLabel=Label(text="Q.1",bg="white", fg="blue", font=('Showcard Gothic', 22, 'bold'))
questionNumberLabel.place(relx=0.26, rely=0.38, anchor='ne')

save = Button(text="Save & Continue", bg="green", fg="white", font=('Showcard Gothic', 12, 'bold'),width=15, height=1,command=save)
save.place(relx=0.22, rely=0.88, anchor='nw')

finish = Button(text="Finish attempt", bg="red", fg="black", font=('Showcard Gothic', 12, 'bold'),width=15, height=1,command=finish)
finish.place(relx=0.57, rely=0.88, anchor='nw')

timeLabel = Label(bg="#F5F5F5", fg="black", font=('Showcard Gothic', 20, 'bold'))
timeLabel.place(relx=0.8, rely=0.25, anchor='ne')

questionLabel=Label(bg="white", fg="black", font=('Showcard Gothic', 15, 'bold'),wraplengt=500)
questionLabel.place(relx=0.81, rely=0.38, anchor='ne')

def countdown(count):
    global name, correct, wrong, score
    timeLabel['text'] = ("{0} second".format(count))
    if count > 0:
        screen2.after(1000, countdown, count-1)
    else:
        Database.insert(name, correct, wrong, score)
        screen2.destroy()
        pygame.mixer.music.stop()
        import result
        result.screen3.mainloop()
def Questions():
    Database.getQuestions(1)
    Database.getA(1)
    Database.getB(1)
    Database.getC(1)
    Database.getD(1)
    questionLabel["text"] = Database.question
    A_radio["text"] = Database.A
    B_radio["text"] = Database.B
    C_radio["text"] = Database.C
    D_radio["text"] = Database.D
def check(Qnum):
    if Qnum == 1 and r.get() == 3:
        return True
    if Qnum == 2 and r.get() == 1:
        return True
    if Qnum == 3 and r.get() == 4:
        return True
    if Qnum == 4 and r.get() == 1:
        return True
    if Qnum == 5 and r.get() == 2:
        return True
    if Qnum == 6 and r.get() == 3:
        return True
    if Qnum == 7 and r.get() == 4:
        return True
    if Qnum == 8 and r.get() == 3:
        return True
    if Qnum == 9 and r.get() == 4:
        return True
    if Qnum == 10 and r.get() == 3:
        return True
    else:
        return False

Questions()
countdown(60)

screen2.mainloop()