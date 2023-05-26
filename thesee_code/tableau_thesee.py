# pip install numpy
# pip install matplotlib

import numpy as np
import matplotlib.pyplot as plt

tableau_des_x=[1, 3, 4, 6]
tableau_des_y=[2, 3, 5, 1]

fig, ax = plt.subplots()
ax.plot(tableau_des_x, tableau_des_y)

plt.show()
