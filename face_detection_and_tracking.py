import numpy as np
import cv2
import sys
import os

# This automatically locates the cascade files within OpenCV

# This automatically locates the cascade files within OpenCV

# Setup Classifiers
face_cascade=cv2.CascadeClassifier(r'./cv_data/haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(r'./cv_data/haarcascade_eye_tree_eyeglasses.xml')
try:
    #check cam init status
    cam=cv2.VideoCapture(0)
    #cam.set(3, 1280)

    #cam.set(4, 720)
    cam.set(15, 2.0)
    if(cam.isOpened()):
        print('Grabbing Camera ..')
		# Uncomment and adjust according to your webcam capabilities
		#webcam.set(cv2.CAP_PROP_FPS,30);
		#webcam.set(cv2.CAP_PROP_FRAME_WIDTH,1024);
		#webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,768);
    else:
        print('Error: Camera could not be opened')
        exit(1)
    while (True):
        # Read each frame in video stream
        ret, frame = cam.read()
        # Perform operations on the frame here
        # First convert to Grayscale
        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Next run filters
        gray=cv2.equalizeHist(gray)
        # Uncomment for Debug if needed
        # cv2.imshow('Grayscale', gray)
        # Face detection using Haar Cascades
        # Detects objects of different sizes in the input image which are returned as a list of rectangles.
        # cv2.CascadeClassifier.detectMultiScale(image[,scaleFactor[,minNeighbors[,flags[,minSize[,maxSize]]]]])
        faces = face_cascade.detectMultiScale(gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        # Draw the rectangles around detected Regions of Interest [ROI] - faces
        # cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]])
        out = frame.copy()
        for(x,y,w,h) in faces:
            cv2.rectangle(out, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = out[y:y + h, x:x + w]
            # Since eyes are a part of face, limit eye detection to face regions to improve accuracy
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                # Draw the rectangles around detected Regions of Interest [ROI] - faces
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        cv2.imshow('Facetracker', out)
        # Wait for Esc Key to quit
        if cv2.waitKey(5) == 27:
            break
    # Release all resources used
    cam.release()
    cv2.destroyAllWindows()


except cv2.Error as e:
    print('OpenCV Error, code = ', e.code)

