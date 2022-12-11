import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

img = cv2.imread('./image/son.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,1.1,4)

for(x, y, w, h) in faces:
    cv2.rectangle(img, (x, y),(x + w,y + h), (255, 0, 0), 2)
    face_gray = gray[y:y+h, x:x+w]
    face_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(face_gray, 1.01, 2)
    smile = smile_cascade.detectMultiScale(face_gray, 1.2,4, minSize = (50,20))

    

    for(ex, ey, ew, eh) in eyes:
        cv2.rectangle(face_color, (ex, ey), (ex + ex, ey + eh), (0, 255, 0), 2)

    for(sx, sy, sw, sh) in smile:
        print(sx,sy,sw,sh)
        cv2.rectangle(face_color, (sx, sy), (sx + sx, sy + sh), (0, 255, 0), 2)
    

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destoryAllWindows()
