'''
Sample 10 is a basic Face and Eye Detection program that uses OpenCV to analyze
an image and detect human faces and eyes. The detected areas or Regions of
Interest (ROI) are demarcated with rectangles. The program uses the OpenCV
built-in pre-trained Haar feature-based cascade classifiers in order to perform this task.
'''

import cv2
import numpy as np

# This section selects the Haar Cascade Classifer File to use
# Ensure that the path to the xml files are correct
# In this example, the files have been copied to the local folder
#face_cascade = cv2.CascadeClassifier(r'./cv_data/haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(r'./cv_data/haarcascade_frontalcatface.xml')
eye_cascade = cv2.CascadeClassifier(r'./cv_data/haarcascade_eye.xml')
# Some Additional Samples - Only one imread should be active. So be sure to comment out all others.
# Image download URL - http://blogs.intel.com/iot/files/2016/04/ASBRparticpants.jpg
#img = cv2.imread('ASBRparticpants.jpg')
# Image download URL - http://blogs.intel.com/iot/files/2016/09/bmw-group-intel-mobileye-3.jpg
#img = cv2.imread(r'./cv_img/bmw-group-intel-mobileye-3.jpg')
# Image download URL - https://upload.wikimedia.org/wikipedia/commons/1/17/Intel_Board_of_Directors.jpg
img = cv2.imread(r'./cv_img/Intel_Board_of_Directors.jpg')
img = cv2.imread(r'./cv_img/cat_03.jpg')
try:
    #img = cv2.imread(r'./cv_img/bmw-group-intel-mobileye-3.jpg')
    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Face detection using Haar Cascades
    # Detects objects of different sizes in the input image. The detected objects are returned as a list of rectangles.
    # cv2.CascadeClassifier.detectMultiScale(image[,scaleFactor[,minNeighbors[,flags[,minSize[,maxSize]]]]]) -> objects
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Draw the rectangles around detected Regions of Interest [ROI] - faces
    # cv2.rectangle(img, pt1, pt2, color[, thickness[, lineType[, shift]]]) -> img
    i=1
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(img, "Cat #{}".format(i + 1), (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.55, (0, 0, 255), 2)
        i=i+1
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]
        # Since eyes are a part of face, limit eye detection to face regions to improve accuracy
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            # Draw the rectangles around detected Regions of Interest [ROI] - eyes
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Display the result
    cv2.imshow('img', img)
    # Show image until dismissed using GUI exit window
    cv2.waitKey(0)
    # Release all resources used
    cv2.destroyAllWindows()

except cv2.Error as e:
    print('OpenCV Error, code=', e.code)