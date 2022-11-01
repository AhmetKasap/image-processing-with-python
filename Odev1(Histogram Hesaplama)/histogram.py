import numpy as np
import matplotlib.pyplot as plt
import cv2

im = cv2.imread('img.jpg')
vals = im.mean(axis=2).flatten()
counts, bins = np.histogram(vals, range(257))
plt.bar(bins[:-1] - 0.5, counts, width=1, edgecolor='none')
plt.xlim([-0.5, 255.5])
plt.show()
