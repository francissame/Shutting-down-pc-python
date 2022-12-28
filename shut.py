import requests 
import cv2
import numpy as np
import imutils

url = "http://192.168.43.11/shot.jpg"

while True:
    imgResp = requests.get(url)
    imgArr = np.array(bytearray(imgResp.content), dtype=np.uint8)
    img = cv2.imdcode(imgArr, -1)
    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("AndriodCam", img)

    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
