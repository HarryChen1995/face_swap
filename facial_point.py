import dlib
import numpy as np
from skimage import io

predictor_path = "shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

img = io.imread("1.jpg")

dets = detector(img)

#output face landmark points inside retangle
#shape is points datatype
#http://dlib.net/python/#dlib.point
for k, d in enumerate(dets):
    shape = predictor(img, d)

with open("1.jpg.txt","w") as f:
    for b in range(68):
        f.write(str(shape.part(b).x)+" " +str(shape.part(b).y)+"\n")
    f.close()