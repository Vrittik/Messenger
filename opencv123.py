import cv2
import numpy as np
import time

def face_detect(loc):
    img=cv2.imread(loc)
    face_detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 2, 5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imwrite(loc,img)

#
# eye_detector=cv2.CascadeClassifier("haarcascade_eye.xml")
#
# img=cv2.imread("temp/37721585_1694801533967944_1337304785631576064_n.jpg")
#
# #img=np.zeros((400,400,3),np.uint8)
# gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# faces=face_detector.detectMultiScale(gray,1.3,5)
#     #print(faces)
# for (x,y,w,z) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+z),(0,0,255),4)
#
#     roi_color = img[y:y + z, x:x + w]
#     roi_gray=cv2.cvtColor(roi_color,cv2.COLOR_BGR2GRAY)
#     eyes=eye_detector.detectMultiScale(roi_gray,1.3,5)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ex+eh),(0,255,0),2)
# cv2.imshow("image",img)
    #cv2.imwrite("images/"+str(count)+"-image.jpg",img)
   # count+=1
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()