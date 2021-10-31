from skimage import io, filters, color, measure
import numpy as np
import matplotlib.pyplot as plt

PLANES = (
    'samolot01.jpg',
    'samolot08.jpg', 
    'samolot09.jpg', 
    'samolot10.jpg', 
    'samolot11.jpg', 
    'samolot17.jpg'
)


def get_contours(image):
    return measure.find_contours(image)


def prepare_image(image):
    img = color.rgb2gray(image)
    return filters.gaussian(img, sigma=2)


def main():
    plt.figure(figsize=(12, 6))
    for i in range(len(PLANES)):
        plt.subplot(2, 3, i+1)
        image = io.imread(PLANES[i])
        h, w = image.shape[0], image.shape[1]
        black_img = np.zeros((h, w))
        image = prepare_image(image)
        contours = measure.find_contours(image)

        plt.imshow(black_img, cmap='gray')

        for contour in contours:
            plt.plot(contour[:, 1], contour[:, 0], linewidth=1, color='w')
        
        plt.xticks([])
        plt.yticks([])

    plt.savefig('simple_contour.pdf')


if __name__ == '__main__':
    main()