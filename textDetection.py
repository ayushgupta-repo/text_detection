# importing modules or libraries

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# reading image
img = cv2.imread('t2.png')

# pytesseract accepts RGB value and opencv is in BGR so converting image into RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# fetching text from the image
# print(pytesseract.image_to_string(img))

# detecting each character as per the sequence x, y, w, h (w and h are the diagonal points of the bounding box not actual width and height)
# print(pytesseract.image_to_boxes(img))

# getting image height and width
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    # print(b)
    b = b.split(' ')
    print(b)

    # extracting informations
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])

    # image, (x, hImg-y), (width, hImg-y), (RGB color), thickness
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 1)

    # labeling characters around their blocks
    cv2.putText(img, b[0], (x, hImg-y+25),
                cv2.FONT_HERSHEY_COMPLEX, 0.5, (50, 50, 255), 1)

# showing image and creating wait key to infinity until close button is clicked
cv2.imshow('Result', img)
cv2.waitKey(0)
