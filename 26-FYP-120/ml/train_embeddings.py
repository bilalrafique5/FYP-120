import os
import numpy as np
from app.services.face_detector import detect_faces
from app.services.face_embedder import get_embedding
from app.core.config import EMBEDDINGS_DIR

RAW_DIR="datasets/raw/"
EMBEDDINGS_FILE=os.path.join(EMBEDDINGS_DIR, "student_embeddings.npy")

if not os.path.exists(EMBEDDINGS_DIR):
    os.makedirs(EMBEDDINGS_DIR)
    
embeddings=[]
student_ids=[]

for student_folder in os.listdir(RAW_DIR):
    path=os.path.join(RAW_DIR,student_folder)
    if not os.path.isdir(path):
        continue
    for img_file in os.listdir(path):
        img_path=os.path.join(path, img_file)
        faces=detect_faces(img_path)
        if len(faces)==0:
            continue
        emb=get_embedding(faces[0])
        if emb is not None:
            embeddings.append(emb)
            student_ids.append(student_folder)
            
np.save(EMBEDDINGS_FILE, {"student_ids":student_ids, "embeddings":embeddings})
print(f"Saved embeddings for {len(student_ids)} students to {EMBEDDINGS_FILE}")

            
