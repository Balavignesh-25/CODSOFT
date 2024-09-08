import cv2

alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(alg)


cam = cv2.VideoCapture(0)

while True:
    ret, img = cam.read()
    if not ret:
        print("Error: Failed to read frame from camera.")
        break

    if img is None:
        print("Error: Received empty frame from camera.")
        continue


    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(grayimg, 1.3, 4)


    for (x, y, w, h) in faces:
        
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(img, "Face", (x, y - 10), font, 0.5, (255, 255, 255), 1)

 
    cv2.imshow("Face Detection", img)


    key = cv2.waitKey(1)
    if key == 27:
        break


cam.release()
cv2.destroyAllWindows()
