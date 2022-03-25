from lib import *
face_cascade=cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)

while True:
    ret,img=cap.read()

    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray)

    for(x,y,w,h)in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('Face & Eye Detection',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()