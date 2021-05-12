from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_blade_comparison_graph():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  xp = np.linspace(x[0], x[len(x)-1], 1000)

  threebladey = np.array([0.056,0.228,0.516,0.924,1.445,2.084,2.836,3.731,4.116,5.818,7.052,8.37,9.845,11.401])
  fourbladey = np.array([0.078,0.185,0.606,1.018,1.586,2.333,3.319,4.084,6.014,7.452,9.267,11.191,12.741,15.676])
  fivebladey = np.array([0.0822,0.332,0.546,1.015,1.527,2.202,3.077,4.091,5.114,6.105,7.76,8.834,10.752,12.1])
  sixbladey = np.array([])
  sevenbladey = np.array([0.0364,0.1468,0.42,0.583,1.093,1.215,1.81,2.384,2.641,3.956,4.644,5.404,6.357,8.666])
  eightbladey = np.array([0.034,0.142,0.423,0.571,1.161,1.521,1.811,2.3,3.401,4.222,4.3,5.298,6.197,9.14])



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