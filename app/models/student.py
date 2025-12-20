from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class StudentModel(BaseModel):
    student_id:str
    name:str
    embedding:Optional[List[float]]=[]
    created_at:Optional[datetime]=datetime.utcnow()