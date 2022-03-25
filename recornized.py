import cv2

import lib
from lib import *

face_cascade=cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("./recognizer/trainingData.yml")
def getProfile(id):
    connect = sqlite3.connect(lib.path_database)
    query = "SELECT * FROM people WHERE id ="+str(id)
    cursor = connect.execute(query)
    profile = None
    for row in cursor:
        profile = row
    connect.close()
    return profile
cam = cv2.VideoCapture(0)
while(True):
    ret,frame = cam.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        id,confidence=recognizer.predict(roi_gray)
    if confidence<40:
        profile = getProfile(id)
        if(profile!=None):
            cv2.putText(frame,str(profile[1]),(x,y+h+30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    else:
        cv2.putText(frame,"Unknown",(x,y+h+30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
