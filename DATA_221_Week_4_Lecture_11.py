import matplotlib.pyplot as plt
import numpy

#Histogram
x = [1, 2, 1.5, 2.5, 3, 2, 2, 2.6, 3, 2, 1.5, 2.5]
plt.hist(x, bins = 12, edgecolor = "white")
plt.show()

#Box Plot
y = [1, 2, 1.5, 2.1, 2.2, 2.5, 3, 2, 2, 2.6, 3, 2, 1.5, 2.5, 4]
plt.boxplot(y)
print(numpy.median(y))
print(numpy.mean(y))
plt.show()

