from app.core.database import get_collection
from app.models.attendance import AttendanceModel
from datetime import date

collection=get_collection("attendance")

class AttendanceCRUD:
    def mark_attendance(self, attendance:AttendanceModel):
        collection.insert_one(attendance.dict())
        
    def check_attendance(self, student_id:str, attendance_date:date):
        return collection.find_one({"student_id":student_id, "date":attendance_date})