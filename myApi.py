from fastapi import FastAPI

app = FastAPI()

student = {
    1 : {
        "name":"viche",
        "university": "Rupp",
    }
}

@app.get("/")
def index():
    return {"name":"Welcome to the Home page"}

@app.get("/get-student/")
def getStudentByID(studentID: int):
    return student[studentID]