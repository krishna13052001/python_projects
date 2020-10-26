# reading the face

import face_recognition
try:
    img=face_recognition.load_image_file("C:/Users/jvskr/Desktop/python projects/screenshot1.jpg")
    loc=face_recognition.face_loacations(img)
    print(loc)
except Exception as e:
    print("no face has beem decteted!!1")