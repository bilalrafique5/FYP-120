from fastapi import FastAPI
from app.api import students, attendance

app=FastAPI(title="Human Face Recognition Attendance System ")

app.include_router(students.router, prefix="/students", tags=["Students"])
app.include_router(attendance.router, prefix="/attendance", tags=["Attendance"])



@app.get("/")
def root():
    return {"message":"Welcome to Face Recognition Attendance System"}

