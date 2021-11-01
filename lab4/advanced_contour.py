import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

from skimage import io, filters, color, measure, feature
from random import randint


PLANES = (
    'samolot00.jpg',
    'samolot01.jpg',
    'samolot02.jpg',
    'samolot03.jpg',
    'samolot04.jpg', 
    'samolot05.jpg',  
    'samolot07.jpg', 
    'samolot08.jpg',
    'samolot09.jpg',
    'samolot10.jpg',
    'samolot11.jpg',
    'samolot12.jpg',
    'samolot13.jpg',
    'samolot14.jpg',
    'samolot15.jpg',
    'samolot16.jpg',
    'samolot17.jpg',
    'samolot18.jpg',
)


COLORS = (
    (0, 204, 0), (0, 0, 204), (204, 0, 0),
    (0, 255, 255), (255, 0, 255), (255, 153, 0), 
    (0, 179, 179), (144,56,120), (77,145,23),
    (45,14,78), (70, 110, 232), (73, 242, 145), 
    (219, 212, 76), (242, 141, 73), (227, 65, 232),
    (98,156,45), (6,250,15), (11,15,166),
)


def bgr2rgb(image):
    return cv.cvtColor(image, cv.COLOR_BGR2RGB)


def to_gray(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)


def get_contours_and_hierarchy(image):
    img_gray = to_gray(image)
    img_blur = cv.medianBlur(img_gray, 7)
    img = cv.Canny(image=img_blur, threshold1=55, threshold2=200)
    img = cv.morphologyEx(img, cv.MORPH_CLOSE, cv.getStructuringElement(cv.MORPH_ELLIPSE, (21,21)))
    contours, hierarchy = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    return contours, hierarchy


def get_major_contours(contours, hierarchy):
    major_contours = []
        
    if len(contours) == 1:
        major_contours.append(contours[0])
    
    for k in range(len(contours)):
        if hierarchy[0][k][2] != -1:
            major_contours.append(contours[k])
    
    return tuple(major_contours)


def draw_contours_and_centroids(image, major_contours):
    for j, c in enumerate(major_contours, start=0):
        M = cv.moments(c)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.drawContours(image, [c], -1, COLORS[j % 18], 7)
            cv.circle(image, (cx, cy), 7, (255, 255, 255), -1)


def main():
    plt.figure(figsize=(10, 20))
    for i in range(len(PLANES)):
        # Create a subplot
        plt.subplot(6, 3, i+1)

        # Read and prepare image
        im = cv.imread(PLANES[i])
        im = bgr2rgb(im)

        # Get contours
        contours, hierarchy = get_contours_and_hierarchy(im)
        major_contours = get_major_contours(contours, hierarchy)
        
        # Draw and plot
        draw_contours_and_centroids(im, major_contours)
        plt.imshow(im)

        # Remove axis ticks
        plt.xticks([])
        plt.yticks([])

    plt.savefig('advanced_contour.pdf')
    

if __name__ == '__main__':
    main()