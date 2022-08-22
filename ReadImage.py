import cv2

img = cv2.imread("./temp/ChatBot-01.png")

cv2.imshow("Display Image", img)

gray_img = cv2.cvtColor(img,cv2.COLOR_RB2GRAY)

cv2.imshow("Gray Scale", gray_img)
print(gray_img)
cv2.waitKey(0)
