from api import *
import matplotlib.pyplot as plt
import numpy as np


def plot_filetli_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  y = np.array([0.061,0.24,0.56,0.98,1.54,2.36,2.98,3.95,4.99,6.17])

  x1 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "o", label="filetli")
  plt.plot(xp, np.polyval(x1, xp), "b--")

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,1,2,3,4,5,6,7,8])

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    if y[i] < 0.5:
      plt.annotate(y[i], xy=(x[i], y[i]+0.5))
    else:
      plt.annotate(y[i], xy=(x[i], y[i]-0.5))

  plt.savefig("filetli.png")

  plt.legend(loc="upper left")
  plt.show()