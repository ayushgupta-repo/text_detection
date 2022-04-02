# importing modules or libraries

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# reading image
img = cv2.imread('t1.png')

# pytesseract accepts RGB value and opencv is in BGR so converting image into RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# showing image and creating wait key to infinity until close button is clicked
cv2.imshow('Result', img)
cv2.waitKey(0)
