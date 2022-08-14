from PIL import Image
import cv2 as cv
import numpy as np
# EDGE DETECTION:
LAPLACIAN_OF_GAUSSIAN = [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
def apply_kernel(gray,MAXX,MAXY,kernel):
    out =  np.arange((MAXX)*(MAXY)).reshape((MAXY),(MAXX)).astype(np.uint8)
    for iy, ix in np.ndindex(gray.shape):
        if iy==0 or ix==0 or iy==MAXY-1 or ix==MAXX-1:
            continue
        else:
            out[iy][ix] =  255 if (gray[iy,ix]*8 - gray[iy-1,ix-1] - gray[iy-1,ix] - gray[iy-1,ix+1] -
            gray[iy,ix-1] - gray[iy,ix+1] - gray[iy+1,ix-1]  - gray[iy+1,ix]  - gray[iy+1,ix+1])>100 else 0
        
    return out

img = Image.open("connect-4.jpg")
pixels = img.load()
cv2_img = np.asarray(img, dtype=np.uint8)
img_gray = cv.cvtColor(cv2_img, cv.COLOR_BGR2GRAY)
# edges = cv.Canny(img_gray,100,180)
edges = apply_kernel(img_gray,img.width,img.height,LAPLACIAN_OF_GAUSSIAN)
cv.imwrite("EDGES.png",edges)