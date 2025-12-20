from fastapi import APIRouter, HTTPException
from app.models.attendance import AttendanceModel
from app.crud.attendance_crud import AttendanceCRUD
from datetime import date


router=APIRouter()
crud=AttendanceCRUD()


@router.post("/mark")
def mark_attendance(attendance:AttendanceModel):
    today=date.today()
    if crud.check_attendance(attendance.student_id,today):
        raise HTTPException(status_code=400, detail="Attendance alrady marked")
    crud.mark_attendance(attendance)
    return {"message":"Attendance marked successfully"}