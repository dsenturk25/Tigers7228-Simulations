from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_first_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])

  y1 = np.array([0.081, 0.33, 0.75, 1.36, 2.08, 3.05, 4.19, 5.44, 6.76, 8.38])
  y2 = np.array([0.061, 0.24, 0.56, 0.98, 1.54, 2.36, 2.98, 3.95, 4.99, 6.17])

  p1 = np.polyfit(x, y1, 1)
  p2 = np.polyfit(x, y1, 4)

  p3 = np.polyfit(x, y2, 1)
  p4 = np.polyfit(x, y2, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y1, "go", label="Filetsiz")
  plt.plot(x, y2, "bo", label="Filetli")
  plt.plot(xp, np.polyval(p2, xp), "g-")
  plt.plot(xp, np.polyval(p4, xp), "b-")

  plt.title("RPM vs. Thrust", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,2,4,6,8,10])

  slope1 = np.polyfit(np.log(x), np.log(y1), 1)
  slope2 = np.polyfit(np.log(x), np.log(y2), 1)

  print("Filetsiz slope:", slope1[0]) 
  print("Filetli slope:", slope2[0]) 

  for i in range(0, len(y1)):
    plt.annotate(y1[i], xy=(x[i], y1[i]+0.5))

  for i in range(0, len(y2)):
    plt.annotate(y2[i], xy=(x[i], y2[i]-0.5))

  plt.legend(loc='upper left')

  plt.savefig("filetlivsfiletsiz.png")
  plt.show()