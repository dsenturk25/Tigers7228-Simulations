from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_blade_comparison_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  xp = np.linspace(x[0], x[len(x)-1], 1000)

  threebladey = np.array([0.069,0.278,0.655,1.178,1.798,2.627,3.385,4.526,5.848,7.126])
  fourbladey = np.array([0.061,0.297,0.625,1.204,1.866,2.692,3.637,4.776,5.867,7.701])
  fivebladey = np.array([0.0822,0.332,0.546,1.015,1.527,2.202,3.077,4.091,5.114,6.105])
  sixbladey = np.array([0.085,0.341,0.776,1.371,2.148,3.135,4.062,5.52,6.994,8.61])

  threeblade = np.polyfit(x, threebladey, 3)
  fourblade = np.polyfit(x, fourbladey, 3)
  fiveblade = np.polyfit(x, fivebladey, 3)
  sixblade = np.polyfit(x, sixbladey, 3)

  plt.plot(x, threebladey, "bo", label="3 blade")
  plt.plot(x, fourbladey, "go", label="4 blade")
  plt.plot(x, fivebladey, "ro", label="5 blade")
  plt.plot(x, sixbladey, "yo", label="6 blade")

  plt.plot(xp, np.polyval(threeblade, xp), "b-")
  plt.plot(xp, np.polyval(fourblade, xp), "g-")
  plt.plot(xp, np.polyval(fiveblade, xp), "r-")
  plt.plot(xp, np.polyval(sixblade, xp), "y-")

  plt.title("RPM vs. Thrust", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10]) 

  plt.legend(loc="upper left")

  plt.savefig("bladecomparison.png")
  plt.show()