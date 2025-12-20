from datetime import date
from app.services.face_matcher import cosine_similarity
from app.services.face_embedder import get_embedding
from app.crud.attendance_crud import AttendanceCRUD

THRESHOLD = 0.6

attendance_crud = AttendanceCRUD()

def process_attendance(face_image, student_embeddings):
    embedding = get_embedding(face_image)
    if embedding is None:
        return "No face embedding found"

    best_score = 0
    best_student = None

    for student_id, saved_embedding in student_embeddings.items():
        score = cosine_similarity(embedding, saved_embedding)
        if score > best_score:
            best_score = score
            best_student = student_id

    if best_score >= THRESHOLD:
        if not attendance_crud.check_attendance(best_student, date.today()):
            attendance_crud.mark_attendance({
                "student_id": best_student,
                "date": date.today(),
                "status": "Present"
            })
            return f"Attendance marked for {best_student}"
        return f"{best_student} already marked"
    
    return "Unknown face detected"
