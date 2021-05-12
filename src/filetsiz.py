from api import *
import matplotlib.pyplot as plt
import numpy as np


def plot_filetsiz_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  y = np.array([0.081,0.33,0.75,1.36,2.08,3.05,4.19,5.44,6.76,8.38])

  x1 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "ro", label="15mm length")
  plt.plot(xp, np.polyval(x1, xp), "r-")

  plt.title("RPM vs. Thrust", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,2,4,6,8,10])

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    if y[i] < 0.3:
      plt.annotate(y[i], xy=(x[i]+1, y[i]+0.2))
    else:
      plt.annotate(y[i], xy=(x[i]+1, y[i]-0.5))

  plt.legend(loc="upper left")

  plt.savefig("filetsiz.png")
  plt.show()