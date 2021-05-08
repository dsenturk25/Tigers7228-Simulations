from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_32vs30_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])

  y1 = np.array([0.07259,0.300,0.679,1.216,1.963,2.718,3.778,4.840,6.136,7.864])
  y2 = np.array([0.0819,0.326,0.687,1.212,1.895,2.989,3.740,5.235,6.641,7.598])

  p1 = np.polyfit(x, y1, 1)
  p2 = np.polyfit(x, y1, 4)

  p3 = np.polyfit(x, y2, 1)
  p4 = np.polyfit(x, y2, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y1, "go", label="30 derece")
  plt.plot(x, y2, "bo", label="32.5 derece")
  plt.plot(xp, np.polyval(p2, xp), "g-")
  plt.plot(xp, np.polyval(p4, xp), "b-")

  plt.title("RPM vs. Thrust", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,2,4,6,8])

  slope1 = np.polyfit(np.log(x), np.log(y1), 1)
  slope2 = np.polyfit(np.log(x), np.log(y2), 1)

  print("30 derece slope:", slope1[0]) 
  print("32.5 derece slope:", slope2[0]) 

  plt.legend(loc='upper left')

  plt.savefig("32vs30.png")
  plt.show()