from insightface.app import FaceAnalysis
import numpy as np


app=FaceAnalysis(name='buffalo_l', providers=['CPUExecutionProvider'])
app.prepare(ctx_id=0, nms=0.4)

def get_embedding(face_image):
    faces=app.get(face_image)
    if len(faces)==0:
        return None
    return faces[0].embedding.tolist()

