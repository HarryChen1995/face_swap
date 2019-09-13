import dlib
import numpy as np
import cv2 
import argparse 
ap = argparse.ArgumentParser(description='Extract Facial Points')
ap.add_argument("--input1",help="path to your picture")
ap.add_argument("--input2",help="path to celebrity picture")
args =ap.parse_args()

predictor_path = "shape_predictor_68_face_landmarks.dat"

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)

img = cv2.imread(args.input1)

dets = detector(img)


for k, d in enumerate(dets):
    shape = predictor(img, d)

with open(args.input1+".txt","w") as f:
    for b in range(68):
        f.write(str(shape.part(b).x)+" " +str(shape.part(b).y)+"\n")
    f.close()

img = cv2.imread(args.input2)

dets = detector(img)


for k, d in enumerate(dets):
    shape = predictor(img, d)

with open(args.input2+".txt","w") as f:
    for b in range(68):
        f.write(str(shape.part(b).x)+" " +str(shape.part(b).y)+"\n")
    f.close()
print("successfully extact facial points")