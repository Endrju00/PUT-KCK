import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import hsv_to_rgb


def main():
    f = open("big.dem", "r")
    lines = f.readlines()
    f.close()

    w, h, distance = map(int, lines[0].split())
    data = []

    for line in lines[1:]:
        data.append(line.split())
    data = np.array(data, dtype='float')

    max_value = np.amax(data)
    min_value = np.amin(data)

    plot_height_map(data, w, h, max_value, min_value)


def hsv2rgb(h, s, v):
    return hsv_to_rgb(np.array([h, s, v]))



def plot_height_map(data, width, height, max_v, min_v):

    def color_map(v, val):
        h = (max_v - v) * 120 / (max_v - min_v)
        s = 1
        return hsv2rgb(h/360, s, val)

    img = np.zeros((width, height, 3))

    for i in range(width):
        for j in range(height):
            val = 0.75
            if j > 0:
                if data[i, j-1] > data[i, j]:
                    val = 0.5
                else:
                    val = 1
            img[i, j] = color_map(data[i, j], val)

    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.savefig('height-map.pdf')


if __name__ == '__main__':
    main()