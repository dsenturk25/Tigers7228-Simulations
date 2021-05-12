from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_angle_comparison_graphs():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])

  thirtyy = np.array([0.07259,0.300,0.679,1.216,1.963,2.718,3.778,4.840,6.136,7.864])
  thirtytwoy = np.array([0.0819,0.326,0.687,1.212,1.895,2.989,3.740,5.235,6.641,7.598])
  thirtyfivey = np.array([0.093,0.371,0.834,1.477,2.32,3.336,4.550,5.935,7.553,9.320])
  thirtyseveny = np.array([0.061, 0.246, 0.559, 0.929, 1.549, 2.180, 2.991, 3.904, 4.713, 7.514])
  fortyy = np.array([0.078,0.316,0.720,1.273,2.005,2.985,3.915,5.093,6.461,8.044])
  fortytwoy = np.array([0.070,0.284,0.651,1.155,1.801,2.668,3.428,4.574,5.810,7.218])
  fortyfivey = np.array([0.069,0.284,0.642,1.154,1.794,2.691,3.463,4.592,5.722,7.335])

  thirty = np.polyfit(x, thirtyy, 4)
  thirtytwo = np.polyfit(x, thirtytwoy, 4)
  thirtyfive = np.polyfit(x, thirtyfivey, 4)
  thirtyseven = np.polyfit(x, thirtyseveny, 4)
  forty = np.polyfit(x, fortyy, 4)
  fortytwo = np.polyfit(x, fortytwoy, 4)
  fortyfive = np.polyfit(x, fortyfivey, 4)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, thirtyy, "bo", label="30 derece")
  plt.plot(x, thirtytwoy, "go", label="32.5 derece")
  plt.plot(x, thirtyfivey, "ro", label="35 derece")
  plt.plot(x, thirtyseveny, "yo", label="37.5 derece")
  plt.plot(x, fortyy, "co", label="40 derece")
  plt.plot(x, fortytwoy, "mo", label="42.5 derece")
  plt.plot(x, fortyfivey, "ko", label="45 derece")

  plt.plot(xp, np.polyval(thirty, xp), "b-")
  plt.plot(xp, np.polyval(thirtytwo, xp), "g-")
  plt.plot(xp, np.polyval(thirtyfive, xp), "r-")
  plt.plot(xp, np.polyval(thirtyseven, xp), "y-")
  plt.plot(xp, np.polyval(forty, xp), "c-")
  plt.plot(xp, np.polyval(fortytwo, xp), "m-")
  plt.plot(xp, np.polyval(fortyfive, xp), "k-")

  plt.title("Thrust vs. RPM", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10]) 

  plt.legend(loc="upper left")

  plt.savefig("anglecomparison.png")
  plt.show()