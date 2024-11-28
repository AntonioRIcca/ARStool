import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(2, 30, 3)
x = range(2, 30, 3)
x_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k']
y = np.arange(0, 20, 2)

ax = plt.subplot()
plt.plot(x, y)
plt.xticks(x)

plt.show()
