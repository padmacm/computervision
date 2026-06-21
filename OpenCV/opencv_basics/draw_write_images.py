import cv2
import numpy as np


azul = 255, 0, 0        
verde = 0, 255, 0        
vermelho = 0, 0, 255        


blank_img = np.zeros((500, 500, 3), dtype='uint8')  


cv2.circle(blank_img, (blank_img.shape[1]//2, blank_img.shape[0]//2), 200, azul, 5)

cv2.line(blank_img, (100,100), (blank_img.shape[1], blank_img.shape[0]), verde, 2)


cv2.putText(blank_img, "Asimov Academy", (3, 253), cv2.FONT_HERSHEY_COMPLEX, 1.5, (255, 255, 255), 3)
cv2.putText(blank_img, "Asimov Academy", (2, 252), cv2.FONT_HERSHEY_COMPLEX, 1.5, vermelho, 3)
cv2.putText(blank_img, "Asimov Academy", (0, 250), cv2.FONT_HERSHEY_COMPLEX, 1.5, azul, 3)

cv2.imshow('blank', blank_img)

cv2.waitKey(0)
