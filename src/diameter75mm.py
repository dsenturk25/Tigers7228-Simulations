from api import *
import matplotlib.pyplot as plt
import numpy as np


def plot_75mm_diameter_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000])
  y = np.array([0.115, 0.302, 0.723, 1.3, 1.973, 3.177, 4.029, 4.884, 6.54, 7.917, 8.843, 11.001, 12.19, 13.17, 15.9])

  p2 = np.polyfit(x, y, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, y, "ro", label="75mm Diameter")
  plt.plot(xp, np.polyval(p2, xp), "r-")

  plt.title("RPM vs. Thrust", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400, 2600, 2800, 3000],fontsize=8)
  plt.yticks([0,2,4,6,8,10,12,14,16],fontsize=10)

  slope = np.polyfit(np.log(x), np.log(y), 1)
  print("Slope:", slope[0]) 

  for i in range(0, len(y)):
    plt.annotate(y[i], xy=(x[i]-1, y[i]-0.5), fontsize="8")

  plt.legend(loc="upper left")

  plt.savefig("diameter: 75mm.png")
  plt.show()