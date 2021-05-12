from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_fortyfivedegree_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  y = np.array([0.069,0.284,0.642,1.154,1.794,2.691,3.463,4.592,5.722,7.335])
  y1 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "ro", label="45 Degree Angle")
  plt.plot(xp, np.polyval(y1, xp), "r-")

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,1,2,3,4,5,6,7,8])

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    if y[i] < 0.3:
      plt.annotate(y[i], xy=(x[i]+1, y[i]+0.2), fontsize="10")
    else:
      plt.annotate(y[i], xy=(x[i]+1, y[i]-0.5))

  plt.legend(loc="upper left")

  plt.savefig("fortyfivedegree.png")
  plt.show()