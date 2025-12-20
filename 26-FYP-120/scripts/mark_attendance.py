import os
import numpy as np
from app.services.face_detector import detect_faces
from app.services.face_embedder import get_embedding
from app.services.face_matcher import cosine_similarity
from app.crud.attendance_crud import  AttendanceCRUD
from datetime import date
from app.core.config import EMBEDDINGS_DIR


EMBEDDINGS_FILE=os.path.join(EMBEDDINGS_DIR, "student_embeddings.npy")
data=np.load(EMBEDDINGS_FILE, allow_pickle=True).item()


attendance_crud=AttendanceCRUD()

def mark_attendance(image_path):
    faces=detect_faces(image_path)
    for face in faces:
        emb=get_embedding(face)
        if emb is None:
            continue
        best_score=0
        best_student=None
        for s_id, s_emb in zip(data["student_ids"],data["embeddings"]):
            score=cosine_similarity(emb,s_emb)
            if score > best_score:
                best_score=score
                best_student=s_id
        if best_score > 0.6: #Threshold
            if not attendance_crud.check_attendance(best_student, date.today()):
                attendance_crud.mark_attendance({
                    "student_id":best_student,
                    "date":date.today(),
                    "status":"Present"
                })
                print(f"Marked attendance for {best_student}")
            else:
                print(f"{best_student} already marked")
        else:
            print("Unknown face detected")
            
mark_attendance("datasets/raw/classroom_image.jpg")
            