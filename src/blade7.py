from api import *
import matplotlib.pyplot as plt
import numpy as np


def plot_7blade_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400])
  y = np.array([0.0364, 0.1468, 0.42, 0.583, 1.093, 1.215, 1.81, 2.384, 2.641, 3.956, 4.644, 5.404])

  p2 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "ro", label="7 blade")
  plt.plot(xp, np.polyval(p2, xp), "r-")

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400],fontsize=8)
  plt.yticks([0,2,4,6],fontsize=10)

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    plt.annotate(y[i], xy=(x[i]-1, y[i]-0.25), fontsize="8")

  plt.legend(loc="upper left")

  plt.savefig("7 blade.png")
  plt.show()