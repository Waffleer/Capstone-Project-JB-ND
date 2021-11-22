import numpy as np 
import matplotlib.pyplot as plt

y_axis = np.array([ 20,  14,  12])

x_labels = np.array(['class 1', 'class 2', 'class 3'])

w = 2
nitems = len(y_axis)
x_axis = np.arange(0, nitems*w, w)    # set up a array of x-coordinates


fig, ax = plt.subplots(1)
ax.bar(x_axis, y_axis, width=w, align='center')
ax.set_xticks(x_axis)
ax.set_xticklabels(x_labels, rotation=90)
plt.show()