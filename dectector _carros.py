import cv2

face_cascade = cv2.CascadeClassifier("cars.xml")
cap = cv2.VideoCapture("videoplayback.mp4")

while True:
    ret, img = cap.read()  # corregido
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  # corregido
    for (x, y, w, h) in faces:  # corregido
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # corregido
    cv2.imshow("img", img)  # corregido
    k = cv2.waitKey(30)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

