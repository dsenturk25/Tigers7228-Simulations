from api import *
import matplotlib.pyplot as plt
import numpy as np


def plot_3blade_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800])
  y = np.array([0.069, 0.278, 0.655, 1.178, 1.798, 2.627, 3.385, 4.526, 5.848, 7.126, 8.554, 10.258, 12.057, 13.627])

  p2 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "ro", label="3 Blade")
  plt.plot(xp, np.polyval(p2, xp), "r-")

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800],fontsize=8)
  plt.yticks([0,2,4,6,8,10,12,14],fontsize=10)

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    plt.annotate(y[i], xy=(x[i]-1, y[i]-0.5), fontsize="8")

  plt.legend(loc="upper left")

  plt.savefig("3_blade.png")
  plt.show()