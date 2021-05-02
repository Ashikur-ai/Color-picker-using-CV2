# Create a function which help to find cordinate of any pixel and its color
import cv2
import numpy as np

def mouse_event(event, x, y, flg, param):
    print("Event==", event)
    print("x==", x)
    print("y==", y)
    print("Flag==", flg)
    print("Param==", param)
    font = cv2.FONT_HERSHEY_COMPLEX_SMALL
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',', y)

        cord = "Cordinate: " + str(x) + ', ' + str(y)
        cv2.putText(img, cord, (x, y), font, 1, (152, 255, 130), 2)
        #cv2.imshow('image', img)

    if event == cv2.EVENT_RBUTTONDOWN:
        b = img[y, x, 0]  # for blue channel is 0
        g = img[y, x, 1]  # for green channel is 1
        r = img[y, x, 2]  # for red channel is 2

        color_bgr = "Color code: " + str(b) + ', ' + str(g) + ', ' + str(r)
        cv2.putText(img, color_bgr, (x, y), font, 1, (152, 255, 130), 2)
       # cv2.imshow('image', img)


cv2.namedWindow(winname='res')

#img = np.zeros((512, 512, 3), np.uint8) # for black screen
img = cv2.imread("b.jpg")
cv2.setMouseCallback("res", mouse_event)

while True:
    cv2.imshow("res", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()
