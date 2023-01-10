import numpy as np

import matplotlib.pyplot as plt

plt.style.use('ggplot')

from pprint import pprint

# apply the function to a meshgrid and add noise
xx, yy = np.mgrid[0:0.5 * np.pi:500j, 0:0.8 * np.pi:500j]

np.random.seed(42)

# generate a regular field
_field = np.sin(xx)**2 + np.cos(yy)**2 + 10

# add noise
np.random.seed(42)

z = _field + np.random.normal(0, 0.15, (500,  500))

plt.imshow(z, cmap='RdYlBu_r')


import skgstat as skg

# random coordinates
np.random.seed(42)

coords = np.random.randint(0, 500, (300, 2))

values = np.fromiter((z[c[0], c[1]] for c in coords), dtype=float)

V = skg.Variogram(coords, values)

V.plot()