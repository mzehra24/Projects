import cv2
#load the haar cascade classifier for eye detection
eye_cascade=cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
#start video capture from the webcam
cap=cv2.VideoCapture(0)
while True:
    #capture frame-by-frame
    ret,frame=cap.read()
    if not ret:
        break
    #convert the frame to grayscale
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Detect eye in the image
    eye = eye_cascade.detectMultiScale(gray)
    #Draw rectangles around detected eyes
    for (ex,ey,ew,eh) in eye:
        cv2.rectangle(frame,(ex,ey), (ex+ew, ey+eh), (0,255,0),2)
    #Display the resulting frame with rectangle around eye
    cv2.imshow('Eye Detection', frame)
    #Break the loop if 'ESC' key is pressed
    if cv2.waitKey(1) & 0xFF ==27: #27 is the ASSCII code for the 'Esc key pressed'
         break
    #Release resources
cap.release()
cv2.destroyALLWindows()

          