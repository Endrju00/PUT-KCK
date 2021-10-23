import numpy as np
import matplotlib.pyplot as plt


f = open("big.dem", "r")
w, h, distance = tuple(map(int, f.readline().split()))
data = [list(map(float, f.readline().split()))]

for line_number in range(h-1):
    line = list(map(float, f.readline().split()))
    new_line = []
    for value in line:
        new_line.append(value)

    data.append(new_line)

data = np.array(data)

plt.imshow(data, cmap='turbo')
plt.colorbar()
plt.show()

f.close()