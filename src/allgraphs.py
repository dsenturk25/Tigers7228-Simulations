from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_all_graphs():

  x = np.array([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])

  filtesizy = np.array([0.081, 0.33, 0.75, 1.36, 2.08, 3.05, 4.19, 5.44, 6.76, 8.38])
  filteliy = np.array([0.061, 0.24, 0.56, 0.98, 1.54, 2.36, 2.98, 3.95, 4.99, 6.17])
  twelwepointfivey = np.array([0.061, 0.246, 0.559, 0.929, 1.549, 2.180, 2.991, 3.904, 4.713, 7.514])

  filtesiz = np.polyfit(x, filtesizy, 2)
  filteli = np.polyfit(x, filteliy, 2)
  twelwepointfive = np.polyfit(x, twelwepointfivey, 2)

  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, filtesizy, "bo", label="Filetsiz")
  plt.plot(x, filteliy, "go", label="Filetli")
  plt.plot(x, twelwepointfivey, "ro", label="12.5 milim")

  plt.plot(xp, np.polyval(filtesiz, xp), "b-")
  plt.plot(xp, np.polyval(filteli, xp), "g-")
  plt.plot(xp, np.polyval(twelwepointfive, xp), "r-")

  plt.title("RPM vs. Thrust", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000])
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10])

  slope_filtesiz = np.polyfit(np.log(x), np.log(filtesizy), 1)
  slope_filteli = np.polyfit(np.log(x), np.log(filteliy), 1)
  slope_twelwepointfive = np.polyfit(np.log(x), np.log(twelwepointfivey), 1)
  print("Slope Filetli:", slope_filteli[0]) 
  print("Slope Filetsiz:", slope_filtesiz[0]) 
  print("Slope 12.5 milim:", slope_twelwepointfive[0]) 

  plt.legend(loc="upper left")

  plt.savefig("all.png")
  plt.show()