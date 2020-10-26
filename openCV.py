import cv2


#to know about image
img=cv2.imread("C:/Users/jvskr/Desktop/python projects/screenshot1.jpg")

print(img.shape)


#to open image
img=cv2.imread("C:/Users/jvskr/Desktop/python projects/screenshot1.jpg",1) # 1 for color and 0 for black and white image
cv2.resize(img,(300,300))
print(img.shape)
cv2.imshow("screenshot",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#to resize image
