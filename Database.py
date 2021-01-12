import mysql.connector

myDB=mysql.connector.connect(
    user='root',
    password='1234',
    host='127.0.0.1',
    database='quizapp'
)

cursor = myDB.cursor()

score=0
name=""
question=""
A=""
B=""
C=""
D=""

# User database functions:
def insert(name,correct,wrong,score):
    query = "INSERT INTO user (name,correct,wrong,score) VALUES (%s,%s,%s,%s)"
    cursor.execute(query, (name,correct,wrong,score))
    myDB.commit()
def getScore():
    global score
    cursor.execute("SELECT score FROM quizapp.user ORDER BY id DESC LIMIT 1")
    for i in cursor.fetchall()[0]:
        score=i
def getName():
    global name
    cursor.execute("SELECT name FROM quizapp.user ORDER BY id DESC LIMIT 1")
    for i in cursor.fetchall()[0]:
        name=i
# question database functions:
def getQuestions(number):
    global question
    cursor.execute("SELECT question FROM sportquestions")
    for i in cursor.fetchall()[number - 1]:
        question=i
def getA(number):
    global A
    cursor.execute("SELECT A FROM sportquestions")
    for i in cursor.fetchall()[number - 1]:
        A = i
def getB(number):
    global B
    cursor.execute("SELECT B FROM sportquestions")
    for i in cursor.fetchall()[number - 1]:
        B = i
def getC(number):
    global C
    cursor.execute("SELECT C FROM sportquestions")
    for i in cursor.fetchall()[number - 1]:
        C = i
def getD(number):
    global D
    cursor.execute("SELECT D FROM sportquestions")
    for i in cursor.fetchall()[number - 1]:
        D = i