#!/usr/bin/env python
# coding: utf-8

# # Libraries are imported

# In[1]:


import cv2


# In[2]:


import os


# In[3]:


import numpy as np


# #### Image is converted to gray image because our classifier takes in a gray image (as it does not matter if image is colored or black and white to detect the image)

#  Haar classifier are trained to detect certain kind of object. 

# # Face Detection

# In[4]:


def faceDetection(test_img):
    gray_img=cv2.cvtColor(test_img,cv2.COLOR_BGR2GRAY)
    face_haar_cascade = cv2.CascadeClassifier('C:\\Users\\DELL\\Documents\\FaceMask\\HaarCascade\\haarcascade_frontalface_default.xml')
    faces=face_haar_cascade.detectMultiScale(gray_img,scaleFactor=1.32,minNeighbors=6)
    
    return faces,gray_img


# Function detectMultiScale is called wgich is going to return the rectangle where the face is detected in that particular test image(test_img). hence gray image is passed.
# Along with it some parameters like scaleFactor is passed to rescale the image (1.32 means we are decresing the size of the image by 32%)
# Images which are bigger in size are likely to be not detected thats why their size is reduced.
# if minNeighbors = 0 then lots of false cases will be detected.
# It should atleast have 5 neighbors to detect true positives.
# faces and gray images will be returned.
# 

# 
# # Training

# In[5]:


def labels_for_training_data(directory): #directory is passes
    faces=[]
    faceID=[]
    
    for path,subdirnames,filenames in os.walk(directory):
        for filename in filenames:
            if filename.startswith("."): #especially for mac
                print("Skipping System File")
                continue
            id=os.path.basename(path) 
            img_path=os.path.join(path,filename)
            print("img_path:", img_path)
            print("id:",id)
            test_img=cv2.imread(img_path) #sometimes it may return None when images doesnot get loaded properly
            if test_img is None:
                print("Image not loaded properly")
                continue
            faces_rect,gray_img=faceDetection(test_img)
            if len(faces_rect)!=1: #In case of multiple faces
                continue
            (x,y,w,h)=faces_rect[0]
            roi_gray=gray_img[y:y+w,x:x+h] #only the face part will be feeded to our classifier
            faces.append(roi_gray)
            faceID.append(int(id))
    return faces,faceID
            


# labels should be only integers.
# os.walk goes recursively to the directory.
# haar classifierr accepts images and labels associated with it.
# 

# In[6]:


#RN we are assuming detection for single face only. There should not be multiple face image in training data.


# ROI = region of index

# In[7]:


def train_classifier(faces,faceID):
    face_recognizer=cv2.face.LBPHFaceRecognizer_create() #local binary pattern histogram. It takes labels as numpy array
    face_recognizer.train(faces,np.array(faceID))
    return face_recognizer


# In[8]:


def draw_rect(test_img,face):  #it will take test image and rectangular coordinates
    (x,y,w,h)=face
    cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,255,0),thickness=4)
    


# In[9]:


def put_text(test_img,text,x,y):
    cv2.putText(test_img,text,(x,y),cv2.FONT_HERSHEY_DUPLEX,4,(255,255,0),3)

