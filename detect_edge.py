import urllib.request
import cv2
import numpy as np

print('''
Attention!
Please follow the followings-
1. Download IP Webcam app from play store.
2. Press Start Server.
3. Allow to operate.
3. Camera will be started and there will be showing a IP address,
   like- http://192.168.1.3:8080
N.B. The Pc and Mobile Phone must be in the same wifi connection!
''')

print("Provide your IP and Port what the app showing-\n")
ip = input("Enter your IP address (Example- 192.168.1.3):  ")
port = input("Enter your Port number (Example- 8080): ")

porturl = 'http://' + ip + ':' + port + '/shot.jpg'

while(1):       
    imgResp = urllib.request.urlopen(porturl)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    frame = cv2.imdecode(imgNp, -1)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([30,150,50]) 
    upper_red = np.array([255,255,180]) 

    mask = cv2.inRange(hsv, lower_red, upper_red) 
    res = cv2.bitwise_and(frame,frame, mask= mask) 


    #cv2.imshow('Original',frame)
    edges = cv2.Canny(frame,100,200) 
    cv2.imshow('Edges',edges) 

    k = cv2.waitKey(5) & 0xFF
    if k == 27: 
        break
  
  
cap.release()
cv2.destroyAllWindows()





