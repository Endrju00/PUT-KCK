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


def color_map(v, max_v, min_v):
    h = (max_v - v) * 120 / (max_v - min_v)
    s = 1
    v = 1
    return hsv2rgb(h/360, s, v)


def plot_height_map(data, width, height, max_v, min_v):
    img = np.zeros((width, height, 3))

    for i in range(width):
        for j in range(height):
            img[i, j] = color_map(data[i, j], max_v, min_v)

    plt.figure(figsize=(10, 10))
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    main()