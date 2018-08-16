import cv2 
from PIL import Image
infile='photo.jpg'

pictPath = r'haarcascade_frontalface_default.xml'
face_cascade= cv2.CascadeClassifier(pictPath)
cv2.namedWindow('Photo')
cap = cv2.VideoCapture(0)
while(cap.isOpened()):
    ret, img = cap.read()
    cv2.imshow('Photo', img)
    if ret == True:
        key = cv2.waitKey(200)
        if key == ord('a'):
            cv2.imwrite(infile, img)
            break
cap.release()            

faces = face_cascade.detectMultiScale(img, scaleFactor=1.2, minNeighbors=3, minSize=(20,20))
# 標註右下角底色黃色
cv2.rectangle(img, (img.shape[1]-120, img.shape[0]-20), (img.shape[1], img.shape[0]), (0,255,255),-1)
# 標註找到多少人臉
cv2.putText(img, 'Find '+ str(len(faces)) + ' face', (img.shape[1]-110,img.shape[0]-5), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0), 1)


num=1
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
    filename = 'faceout' + str(num) +'.jpg'
    image = Image.open(infile)
    imageCrop = image.crop((x,y,x+w,y+h))
    imageResize = imageCrop.resize((150,150), Image.ANTIALIAS)
    # imageResize = imageCrop.resize((150,150), Image.LANCZOS)
    imageResize.save(filename)
    num +=1

cv2.namedWindow('Face Detect',cv2.WINDOW_NORMAL)
cv2.imshow('Face Detect',img)
cv2.waitKey(10000)                                    #wait key for 10 sec