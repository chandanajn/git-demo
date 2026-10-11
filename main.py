from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Student Management API")


class Student(BaseModel):
    name: str
    age: int
    course: str


students = []


@app.get("/")
def home():
    return {"message": "Student Management API is running"}


@app.get("/students")
def get_students():
    return students


@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    return students[student_id]


@app.post("/students")
def create_student(student: Student):
    students.append(student.model_dump())

    return {
        "message": "Student created successfully",
        "student": student
    }


@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    students[student_id] = student.model_dump()

    return {
        "message": "Student updated successfully",
        "student": student
    }


@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id < 0 or student_id >= len(students):
        raise HTTPException(status_code=404, detail="Student not found")

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted successfully",
        "student": deleted_student
    }