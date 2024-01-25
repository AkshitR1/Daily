import cv2
from PIL import Image
from util import get_limits  

yellow = [0, 255, 255]  

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerlim, upperlim = get_limits(color=yellow)
    
    mask = cv2.inRange(hsvImg, lowerlim, upperlim)

    mask1 = Image.fromarray(mask)

    bbox = mask1.getbbox()


  
    if bbox is not None:
        x1, y1, x2, y2 = bbox
        frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
