from pydantic import BaseModel
from datetime import date


class AttendanceModel(BaseModel):
    student_id:str
    date:date
    status:str="Present"
    