from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_length_comparison_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000,2200,2400,2600,2800])
  xp = np.linspace(x[0], x[len(x)-1], 1000)

  niney = np.array([0.037,0.06,0.261,0.466,0.726,1.043,1.102,1.209,1.578,1.704,1.876,1.998,2.4,2.76])
  eleveny = np.array([0.048,0.114,0.356,0.644,0.991,1.667,2.165,2.435,3.794,4.435,5.825,6.937,8.155,9.266])
  thirteeny = np.array([0.067,0.221,0.558,1.059,1.543,2.218,3.313,4.273,5.662,7.573,8.217,9.174,11.408,12.54])
  fifteeny = np.array([0.078,0.185,0.606,1.018,1.586,2.333,3.319,4.084,6.014,7.452,9.267,11.191,12.741,15.676])
  sixteeny = np.array([0.055,0.092,0.518,0.907,1.435,2.664,2.93,3.831,4.146,5.423,7.05,7.714,10.727,12.332])
  eighteeny = np.array([0.061,0.317,0.572,0.952,1.497,2.433,2.866,3.737,5.379,6.47,8.193,9.939,11.574,13.503])
  nineteeny = np.array([0.61,0.327,0.614,1.02,1.59,2.735,3.125,4.146,5.763,6.878,8.705,10.256,12.06,12.893])

  nine = np.polyfit(x, niney, 2)
  eleven = np.polyfit(x, eleveny, 2)
  thirteen = np.polyfit(x, thirteeny, 2)
  fifteen = np.polyfit(x, fifteeny, 2)
  sixteen = np.polyfit(x, sixteeny, 2)
  eighteen = np.polyfit(x, eighteeny, 2)
  nineteen = np.polyfit(x, nineteeny, 2)

  plt.plot(x, niney, "bo", label="9.5mm uzuluk")
  plt.plot(x, eleveny, "ro", label="11mm uzuluk")
  plt.plot(x, thirteeny, "go", label="13.5mm uzuluk")
  plt.plot(x, fifteeny, "yo", label="15mm uzuluk")
  plt.plot(x, sixteeny, "co", label="16.5mm uzuluk")
  plt.plot(x, eighteeny, "mo", label="18mm uzuluk")
  plt.plot(x, nineteeny, "ko", label="19.5mm uzuluk")

  plt.plot(xp, np.polyval(nine, xp), "b-")
  plt.plot(xp, np.polyval(eleven, xp), "r-")
  plt.plot(xp, np.polyval(thirteen, xp), "g-")
  plt.plot(xp, np.polyval(fifteen, xp), "y-")
  plt.plot(xp, np.polyval(sixteen, xp), "c-")
  plt.plot(xp, np.polyval(eighteen, xp), "m-")
  plt.plot(xp, np.polyval(nineteen, xp), "k-")

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000,2200,2400,2600,2800])
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]) 

  plt.legend(loc="upper left")

  plt.savefig("lengthcomparison.png")
  plt.show()