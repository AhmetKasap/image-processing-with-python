
'''
import cv2
img = cv2.imread("img.jpg")
cv2.imshow("Orijinal",img)
img_not = cv2.bitwise_not(img)
cv2.imshow("Invert",img_not)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''


import cv2
img = cv2.imread("img.jpg",0)
img_max=0

for i in range(img.shape[0]):  
    for j in range(img.shape[1]):
        if(img[i,j]>img_max):
            img_max=img[i,j]

cv2.imshow("original",img)        
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img[i,j] = img_max-img[i,j]

cv2.imshow("invert",img)
cv2.waitKey()

