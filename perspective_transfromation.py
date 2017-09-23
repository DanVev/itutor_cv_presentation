import cv2
import numpy as np


def get_contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 70, 230)
    cv2.imshow('Canny', canny)
    s, contours, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        max_area = 0.0
        max_contour = None
        for contour in contours:
            c_area = cv2.contourArea(contour)
            if c_area > max_area and 30000.0 < c_area < 100000.0:
                max_area = c_area
                max_contour = contour
        print(max_area)
        if max_contour:
            epsilon = 0.1 * cv2.arcLength(max_contour, True)
            approx = cv2.approxPolyDP(max_contour, epsilon, True)
            cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        cv2.imshow('Image', img)


cam = cv2.VideoCapture(0)
while True:
    _, frame = cam.read()
    # cv2.imshow("frame", frame)
    get_contours(frame)

    cv2.imshow("frame", frame)
    pressed_key = cv2.waitKey(30)
    if pressed_key == 27:
        break
