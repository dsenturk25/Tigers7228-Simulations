from api import *
import matplotlib.pyplot as plt
import numpy as np


def plot_5blade_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2700, 2800])
  y = np.array([0.0822, 0.332, 0.546, 1.015, 1.527, 2.202, 3.077, 4.091, 5.114, 6.105, 7.76, 8.834, 10.752, 11.08, 12.1])

  p2 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "ro", label="5 blade")
  plt.plot(xp, np.polyval(p2, xp), "r-")

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800],fontsize=8)
  plt.yticks([0,2,4,6,8,10,12],fontsize=10)

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    if y[i] == 10.752:
      plt.annotate(y[i], xy=(x[i]-1, y[i]-0.75), fontsize="8")
    else:
      plt.annotate(y[i], xy=(x[i]-1, y[i]-0.5), fontsize="8")

  plt.legend(loc="upper left")

  plt.savefig("5 blade.png")
  plt.show()