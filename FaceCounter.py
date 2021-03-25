from cv2 import cv2
import face_recognition

video_capture = cv2.VideoCapture(0) # captures the video from the default camera

face_location=[] # coordinates of the faces found
faces = 0 # initialize number of faces with 0

while True:
    ret, frame = video_capture.read() # captures the current frame and stores it
    face_location = face_recognition.face_locations(frame) #it gives the faces coordinates
    faces = len(face_location) # number of faces
    people = "People: "+str(faces)  
    for top,right,bottom,left in face_location:
        cv2.rectangle(frame, (left, top), (right,bottom),(0,255,0),2)
        
    cv2.putText(frame,people,(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)   

    cv2.imshow("face_recongition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
