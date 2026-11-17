from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel,Field
from fastapi.responses import RedirectResponse

import sqlite3

def get_connection():
    connection = sqlite3.connect(
        "students.db"
    )
    return connection
templates = Jinja2Templates(
    directory="templates"
)


app = FastAPI()

class Student(BaseModel):
    name:str = Field(max_length=30 , min_length=3)
    age:int = Field(le=30,ge=18)
    gender:str = Field(max_length=10)
    marks:int = Field(le=100,ge=1)
    course:str = Field(max_length=20,min_length=3)
    image:str
    status:int

def create_table():
    connection = get_connection()
    cursor = connection.cursor()

    q = """
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    gender TEXT,
    marks INTEGER,
    course TEXT,
    image TEXT,
    status INTEGER
    )

    """
    cursor.execute(q)
    connection.commit()
    connection.close()

create_table()


@app.get("/")
def home(req:Request):
    connection = get_connection()
    cursor = connection.cursor()
    q = "select * from students"
    cursor.execute(q)
    students = cursor.fetchall()
    connection.close()
    print(students)
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={"stds":students}
    )
@app.get("/students/{std_id}")
def Single_std(req:Request,std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q = "select * from students where id = ?"
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()

    return templates.TemplateResponse(
        request=req,
        name="single-std.html",
        context={
            "std":student
        }
    )

@app.get("/student/add")
def create_std(req:Request):
    return templates.TemplateResponse(
        request=req,
        name="create-std.html",
        context={}
    )

@app.post("/student/add")
def Reciving_std(
    name = Form(),
    age = Form(),
    gender = Form(),
    marks = Form(),
    course = Form(),
    image = Form(),
    status = Form()
    ):

    std_obj =Student(
        name=name,
        age=age,
        gender=gender,
        marks=marks,
        course=course,
        image=image,
        status=status
    )
    values = (std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,bool(std_obj.status))
    print(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,bool(std_obj.status))
    connection = get_connection()
    cursor = connection.cursor()
    q = """
    INSERT INTO students(name,age,gender,marks,course,image,status)
    values(?,?,?,?,?,?,?)
    """
    cursor.execute(q,values)
    connection.commit()
    connection.close()
    return RedirectResponse(url="/")


@app.get("/std/{std_id}")
def Deleting_std(std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q = "DELETE FROM students where id = ?"
    cursor.execute(q,(std_id,))
    connection.commit()
    connection.close()

    return RedirectResponse(url="/")




@app.get("/sdts/update/{std_id}")
def edit_student(req:Request,std_id:int):
    connection = get_connection()
    cursor = connection.cursor()
    q = "select * from students where id = ?"
    cursor.execute(q,(std_id,))
    student = cursor.fetchone()
    connection.close()
    return templates.TemplateResponse(
        request=req,
        name="update.html",
        context={
            "std":student
        }
    )

@app.post("/student/update/{std_id}") 
def upadting_std(
    std_id:int,
    name=Form(),
    age=Form(),
    gender=Form(),
    marks=Form(),
    course=Form(),
    image=Form(),
    status=Form()
    ):
    std_obj =Student(
            name=name,
            age=age,
            gender=gender,
            marks=marks,
            course=course,
            image=image,
            status=status
        )
    # values = (std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,bool(std_obj.status),std_id)
    connection = get_connection()
    cursor = connection.cursor()
    q = """update students set name = ?,age = ?,gender = ?,marks = ?,course = ?,image = ?,status = ? where id = ?"""
    cursor.execute(q,(std_obj.name,std_obj.age,std_obj.gender,std_obj.marks,std_obj.course,std_obj.image,bool(std_obj.status),std_id))
    connection.commit()
    connection.close()
    return RedirectResponse(url="/")


