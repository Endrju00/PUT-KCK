import numpy as np
import matplotlib.pyplot as plt

from skimage import io, filters, color, measure, feature
from random import randint


PLANES = (
    'samolot00.jpg',
    'samolot01.jpg',
    'samolot02.jpg',
    'samolot03.jpg',
    'samolot04.jpg', 
    'samolot05.jpg', 
    'samolot06.jpg', 
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


def get_contours(image):
    return measure.find_contours(image)


def prepare_image(image):
    img = color.rgb2gray(image)
    img = filters.gaussian(img, sigma=2)
    return feature.canny(img, sigma=3)


def random_rgba():
    r = randint(0, 100) / 100
    g = randint(0, 100) / 100
    b = randint(0, 100) / 100
    return (r, g, b, 1)


def main():
    plt.figure(figsize=(12, 6))
    for i in range(len(PLANES)):
        plt.subplot(4, 5, i+1)
        image = io.imread(PLANES[i])
        prep_image = prepare_image(image)
        contours = measure.find_contours(prep_image)

        plt.imshow(image)

        for contour in contours:
            plt.plot(contour[:, 1], contour[:, 0], linewidth=1, color='r')
        
        plt.xticks([])
        plt.yticks([])

    plt.show()


if __name__ == '__main__':
    main()