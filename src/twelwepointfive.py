from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_fourth_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  y = np.array([0.061, 0.246, 0.559, 0.929, 1.549, 2.180, 2.991, 3.904, 4.713, 7.514])

  p1 = np.polyfit(x, y, 1)
  p2 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "o")
  plt.plot(xp, np.polyval(p1, xp), "b--")
  plt.plot(xp, np.polyval(p2, xp), "r-")

  plt.title("RPM vs. Thrust", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,2,4,6,8])

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    plt.annotate(y[i], xy=(x[i]+1, y[i]-0.5))

  plt.savefig("twelwepointfive.png")
  plt.show()