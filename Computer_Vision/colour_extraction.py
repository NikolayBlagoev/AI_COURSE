from math import sqrt
from PIL import Image
import cv2 as cv
import numpy as np
img = Image.open("connect-4.jpg")
pixels = img.load()

# COLOUR EXTRACTION
def distance(x1,y1,z1,x2,y2,z2):
    return sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
def lwup(r,g,b,lower,upper):
    return (r>=lower[0] and r<=upper[0]) and (g>=lower[1] and g<=upper[1]) and (b>=lower[2] and b<=upper[2])
def colour_extract_1(img,pixels):
    mask = np.arange(img.width*img.height).reshape(img.height,img.width).astype(np.uint8)
    for x in range(img.width):
        for y in range(img.height):
            r,g,b = pixels[x,y]
            if distance(r,g,b,253, 231,0)>40:
                mask[y][x]=0
            else:
                mask[y][x]=255
    return mask
def colour_extract_2(img,pixels,lower,upper):
    lower.reverse()
    upper.reverse()
    mask = np.arange(img.width*img.height).reshape(img.height,img.width).astype(np.uint8)
    for x in range(img.width):
        for y in range(img.height):
            r,g,b = pixels[x,y]
            if lwup(r,g,b,lower, upper):
                mask[y][x]=255
            else:
                mask[y][x]=0
    return mask

cv2_img = np.asarray(img,dtype=np.uint8)
cv2_img = cv.cvtColor(cv2_img, cv.COLOR_BGR2RGB)

lower_bound = np.array([0,100,100])
upper_bound = np.array([60,255,255])

# mask = cv.inRange (cv2_img, lower_bound, upper_bound)
# mask = colour_extract_1(img,pixels)
mask = colour_extract_2(img,pixels,[0,180,180],[60,255,255])
cv.imwrite("mask.png",mask)
            
threshold = cv.dilate(mask, None, iterations=1)
cnts, _ = cv.findContours(threshold, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

for c in cnts:
    
    if cv.contourArea(c) < 50 or cv.contourArea(c)>500:
        continue
    (x, y, w, h) = cv.boundingRect(c)
    print(str(x)+str(x+w))
                
    cv.rectangle(cv2_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv.imwrite("COLOURS_IDENTIFIED.png", cv2_img)

