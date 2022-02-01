# knee-rep-counter
 An ML program to count number of knee rep using 
 MEDIAPIPE pose model

**Knee Rep Counter**

**Modules used:**
OpenCV-python 
Mediapipe
Numpy

**Mediapipe model:**
Pose model is used for detections

Model confidence set to 0.5 both detection and tracking, to change that you need to change the value in this line of code:

with mp_pose.Pose(min_detection_confidence = 0.5 ,min_tracking_confidence = 0.5) as pose:



Current program will only count the  user knee rep only if the angle between hip ,knee and  ankle is below 100

To change that you need to change the angle of this line:

	if angle <100 and stage == 'down':

**How video is loaded:**
Video is loaded locally on my linux machine to change to load it from your machine you need to change the path of the video in this one of code:

cap=cv.VideoCapture('/home/kuuhaku/Documents/knee_rep/knee-rep/video/vid.mp4')


**Landmarks:**

Landmark used are : LEFT KNEE, LEFT HIP and LEFT ANKLE
To count other than the angle between knee ,hip and ankle you need to replace LEFT_HIP ,LEFT_ANKLE and LEFT_KNEE in this code to another valid landmark in pose model

hip=[landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y] 

knee=[landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

ankle=[landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]
 
	

And change the values in here in case you rename the variables:

	angle = calangle(hip,knee,ankle)

**How to quit and change output screen name :**

Change the name “feed” if you wanna change the output screen name 
	cv.imshow('feed',img)

Change the ‘q’ here if you wanna exit using different key:
if cv.waitKey(20) & 0xFF == ord('q'):

