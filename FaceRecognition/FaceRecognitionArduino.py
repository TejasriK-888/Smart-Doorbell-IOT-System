import face_recognition #need to instal cmake and dlib libraries too, and you must have C++
import cv2
import numpy as np
import os
import time
import serial

# Connect to Arduino via Serial
arduino = serial.Serial('COM9', 9600)  # Update 'COM9' with your Arduino port
#set the paths for folders
folder = "Stranger" #New File for Strangers
path = 'OwnerFace' #path to the owner faces
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode= face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList



encodeListKnown = findEncodings(images)
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgSmall = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(imgSmall)
    encodeFrame = face_recognition.face_encodings(imgSmall, face_locations)
    face_names = []
    for face_encoding,faceLoc in zip(encodeFrame,face_locations ):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(encodeListKnown, face_encoding)
        name = "Stranger"
        face_distances = face_recognition.face_distance(encodeListKnown, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = classNames[best_match_index]
        face_names.append(name)

    imgSmall = cv2.cvtColor(imgSmall, cv2.COLOR_BGR2RGB)
    for (top, right, bottom, left), name in zip(face_locations, face_names):

        # Draw a box around the face
        if name == "Stranger":
            cv2.rectangle(imgSmall, (left, top), (right, bottom), (0, 0, 255), 2)
            cv2.rectangle(imgSmall, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(imgSmall, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            cv2.imwrite(f'{folder}/stranger.jpg', imgSmall)
            arduino.write(b'0')
        else:
            cv2.rectangle(imgSmall, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(imgSmall, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(imgSmall, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
            arduino.write(b'1')
        print(name)

    cv2.imshow('door', imgSmall)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
cv2.VideoCapture.release()
cv2.destroyAllWindows()





