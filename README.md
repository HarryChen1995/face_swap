# Face Swap 

this project was created to map celebrity's face to a different person between two images using dlib.<br>
<img  height = 450; width = 350; src="src/2.jpg"/>
<img  height = 450; width = 350  src="src/justin_bieber.jpg"/>



# After Facial Mapping:

<img  height = 340, width = 250 src="src/result.jpg"/>

# Requirement:
* python3-opencv
* dlib
* skimage
* numpy  
# Usage:
## Extract Facial Landmarks
```bash
python3 facial_point.py --input1='path to your image'\ 
                         --input2='path to celebrity picture' 
```

## Mapping Face
```bash
python3 faceSwap.py --input1='path to your image'\ 
                         --input2='path to celebrity picture' 
```