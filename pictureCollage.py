# Collage of Edits of a picture

import cv2
import numpy as np
import urllib.request as urllib

def empty(a):
    pass

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = input("Enter image link: ")
headers={'User-Agent':user_agent,}

try:
    request = urllib.Request(url,None,headers)
except ValueError:
    print("Invalid URL")
    exit()
response = urllib.urlopen(request)
img = np.asarray(bytearray(response.read()), dtype="uint8")
img = (cv2.imdecode(img, cv2.IMREAD_COLOR))

if img is None:
    print("test")
imgResize = cv2.resize(img, (480, 270))
kernel = np.ones((5,5), np.uint8)
height = img.shape[1]
width = img.shape[0]

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Gray", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Blur", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Canny", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Dilation", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Erosion", "TrackBars", 0, 255, empty)
cv2.createTrackbar("HSV", "TrackBars", 255, 255, empty)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 0)
imgCanny = cv2.Canny(imgResize, 150, 200)
imgDialation = cv2.dilate(imgCanny, kernel, iterations=2)
imgEroded = cv2.erode(imgResize, kernel, iterations=2)
imgHSV = cv2.cvtColor(imgResize, cv2.COLOR_BGR2HSV)
imgBlank = np.zeros((height, width, 3), np.uint8)

collage = stackImages(0.5, ([imgResize, imgGray, imgBlur], [imgCanny, imgDialation, imgEroded], [imgHSV, imgBlank, imgBlank]))

# cv2.imshow("Image", img)
# cv2.imshow("Resized", imgResize)
cv2.imshow("Collage", collage)

cv2.waitKey(0)
