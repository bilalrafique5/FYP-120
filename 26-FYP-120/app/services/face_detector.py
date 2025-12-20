from mtcnn import MTCNN
import cv2

detector=MTCNN()


def detect_faces(image_path):
    img=cv2.imread(image_path)
    img_rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results=detector.detect_faces(img_rgb)
    
    faces=[]
    for r in results:
        x,y,w,h=r['box']
        faces.append(img_rgb[y:y+h, x:x+w])
    return faces


    