from fastapi import HTTPException, APIRouter
from app.models.student import StudentModel
from app.crud.student_crud import StudentCRUD



router=APIRouter()
crud=StudentCRUD()

@router.post("/register")
def register_student(student:StudentModel):
    if crud.get_student_by_id(student.student_id):
        raise HTTPException(status_code=400, detail="Student already exists")
    crud.create_student(student)
    return {"message":"Student registeres successfully"}


@router.get("/{student_id}")
def get_student(student_id:str):
    student=crud.get_student_by_id(student_id)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student