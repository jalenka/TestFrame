import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

msg = "Hello World"
print(msg)
print(msg)

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.sin(x))       # Plot the sine of each x point
# plt.show()                   # Display the plot


def my_function(x):
  return 5 * x

def test_myanswer():
  assert(my_function(3) == 15)