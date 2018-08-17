import cv2 
from PIL import Image


pictPath = r'haarcascade_frontalface_default.xml'
face_cascade= cv2.CascadeClassifier(pictPath)
cv2.namedWindow('Photo')
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, img = cap.read()
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3, minSize=(20,20))
    # 標註右下角底色黃色
    cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20), (img.shape[1], img.shape[0]), (0,255,255),-1)
    # 標註找到多少人臉
    cv2.putText(img, 'Find '+ str(len(faces)) + ' face', (img.shape[1]-110,img.shape[0]-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)
   
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2) 
     


    cv2.imshow('Photo', img)
    if ret == True:
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

cv2.destroyAllWindows()
cap.release()            






