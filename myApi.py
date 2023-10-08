from fastapi import FastAPI
from enum import Enum

app = FastAPI()

student = {
    "computer_science" : {
        "id":1,
        "name":"viche",
        "university": "Rupp",
        "major": "CS",
    },
    "designer" : {
        "id":2,
        "name":"John",
        "university": "Rupp",
         "major": "Designer",
    }
}

teacher = {
    1 : {
        "id":1,
        "name":"Adam",
        "university": "Rupp",
        "major": "CS",
    },
    2 : {
        "id":2,
        "name":"Will",
        "university": "Rupp",
        "major": "Designer",
    }
}



class StudentMajor(str,Enum):
    Designer = "designer"
    CS = "computer_science"


@app.get("/")
def index():
    return {"name":"Welcome to the Home page"}

@app.get("/Users")
def getAllStudents():
    return student

@app.get("/Student/")
def getStudentByMajor(studentMajor: StudentMajor):
     if studentMajor is StudentMajor.CS:
        return student[studentMajor]
     if studentMajor is StudentMajor.Designer:
        return student[studentMajor]


@app.get("/Teacher/")
def getTeacherByID(id:int):
    return teacher[id]

