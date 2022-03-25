import lib
from lib import *
def insert_update_data(id, name):

    connect = sqlite3.connect(lib.path_database)
    query = "select * from people where id ="+str(id)
    cursor = connect.execute(query)

    isRecordExist = 0
    for row in cursor:
        isRecordExist = 1
    if(isRecordExist == 0):
        query = "INSERT INTO people(id, Name) VALUES("+str(id)+",'"+str(name)+"')"
    else:
        query = "UPDATE people SET Name = '"+str(name)+"' WHERE id = "+str(id)

    connect.execute(query)
    connect.commit()
    connect.close()

face_cascade=cv2.CascadeClassifier('./data/haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
id = input("Enter your ID: ")
name = input("Enter your Name: ")
insert_update_data(id, name)
sampleNum =0
while(True):
  ret, frame = cap.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray)

  for (x, y, w, h) in faces:
     cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
     if not os.path.exists('dataset'):
        os. makedirs('dataset')
     sampleNum += 1
     cv2.imwrite('./dataset/User.'+str(id)+'.'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])

  cv2.imshow('frame', frame)
  cv2.waitKey(100)
  if sampleNum > 100 :
      break;
cap.release()
cv2.destroyAllWindows()