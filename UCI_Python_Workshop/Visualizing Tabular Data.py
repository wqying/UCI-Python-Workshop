# Learning about matplotlib, specifically the matplotlib.pyplot library
# matplotlib is the standard plotting library for python

import numpy  # usually people import numpy as np
import matplotlib.pyplot  # usually people import matplotlib.pyplot as plt

# loading data using numpy, we use "numpy.loadtxt()"
data = numpy.loadtxt(fname='C:/Learning/UCI_Python_Workshop/python-novice-inflammation-data/data/inflammation-01.csv',
              delimiter=',')

image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show()  # shows the plot of "image"

ave_inflammation = numpy.mean(data, axis=0)  # axis=0 means we are working with the rows
ave_plot = matplotlib.pyplot.plot(ave_inflammation)
matplotlib.pyplot.show()  # shows the plot of ave_plot (because we called "matplotlib.pyplot" in ave_plot

# Find the max and min of the data
max_plot = matplotlib.pyplot.plot(numpy.max(data, axis=0))
min_plot = matplotlib.pyplot.plot(numpy.min(data, axis=0))
matplotlib.pyplot.show()  # shows the plot of the max and min

# naming and assigning names to the figures
fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))  # set the figure size
# add subplots to the blank figure canvas
# add_subplot() parameters: (number of rows, number of columns, index of the subplot)
axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.set_ylabel('average')
axes1.plot(numpy.mean(data, axis=0))  # note that we shouldn't straight up use the "ave_plot" variable above
# because we're trying to make this into a subplot in the figure

axes2.set_ylabel('max')
axes2.plot(numpy.max(data, axis=0))

axes3.set_ylabel('min')
axes3.plot(numpy.min(data, axis=0))

fig.tight_layout()  # good practice to have to make the plots closer to each other
matplotlib.pyplot.savefig('inflammation.png')  # use this function to save the plot
matplotlib.pyplot.show()
