from math import radians
import mediapipe as mp
import cv2 as cv
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


def calangle(a,b,c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)
    
    radians = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angle = np.abs(radians*180.0/np.pi)
    
    if angle >180.0:
        angle = 360-angle
    return angle


count = 0
stage= None 
    
cap =cv.VideoCapture('/home/kuuhaku/Documents/knee_rep/knee-rep/video/vid.mp4')
with mp_pose.Pose(min_detection_confidence = 0.5 ,min_tracking_confidence = 0.5) as pose:
 while True:
     isTrue, frame= cap.read()
    
    
     img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
     img.flags.writeable = False
    
     res = pose.process(img)
    
     img.flags.writeable = True
     img = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
     
     try:
         landmarks = res.pose_landmarks.landmark
         hip =[landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]
         knee =[landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]
         ankle =[landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

         
         angle = calangle(hip,knee,ankle)
         
         cv.putText(img,str(angle), 
                    tuple(np.multiply(knee ,[640,480]).astype(int)),
                          cv.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2,cv.LINE_AA
                   )
         
         if angle >160:
             stage ='down'
         if angle <90 and stage == 'down':
             stage = 'up'
             count+=1
             print(count)
     except:
         pass
     
     
     cv.rectangle(img,(0,0),(225,73),(245,117,16), -1)
     cv.putText(img,'KNEE-REPS', (15,12),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv.LINE_AA)
     cv.putText(img,str(count), (10,60),cv.FONT_HERSHEY_SIMPLEX,2,(225,225,225),2,cv.LINE_AA)
     
     cv.putText(img,'STAGE', (115,12),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),1,cv.LINE_AA)
     cv.putText(img,stage, (60,60),cv.FONT_HERSHEY_SIMPLEX,2,(225,225,225),2,cv.LINE_AA)
     
    
     mp_drawing.draw_landmarks(img,res.pose_landmarks,mp_pose.POSE_CONNECTIONS)
    
     
     cv.imshow('feed',img)
     if cv.waitKey(20) & 0xFF == ord('q'):
         break
    
    
 


