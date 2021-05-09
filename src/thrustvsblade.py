from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_thrustvsblade_graphs():

  x = np.array([3,4,5,6])

  test1y = np.array([0.069,0.061,0.0822,0.085])
  test2y = np.array([0.278,0.297,0.332,0.341])
  test3y = np.array([0.655,0.625,0.546,0.776])
  test4y = np.array([1.178,1.204,1.015,1.371])
  test5y = np.array([1.798,1.866,1.527,2.148])
  test6y = np.array([2.627,2.692,2.202,3.135])
  test7y = np.array([3.385,3.637,3.077,4.062])
  test8y = np.array([4.526,4.776,4.091,5.52])
  test9y = np.array([5.848,5.867,5.114,6.994])
  test10y = np.array([7.126,7.701,6.105,8.61])

  test1 = np.polyfit(x, test1y, 4)
  test2 = np.polyfit(x, test2y, 4)
  test3 = np.polyfit(x, test3y, 4)
  test4 = np.polyfit(x, test4y, 4)
  test5 = np.polyfit(x, test5y, 4)
  test6 = np.polyfit(x, test6y, 4)
  test7 = np.polyfit(x, test7y, 4)
  test8 = np.polyfit(x, test8y, 4)
  test9 = np.polyfit(x, test9y, 4)
  test10 = np.polyfit(x, test10y, 4)
  
  xp = np.linspace(x[0], x[len(x)-1], 1000)

  plt.plot(x, test1y, "bo", label="200 rpm")
  plt.plot(x, test2y, "go", label="400 rpm")
  plt.plot(x, test3y, "ro", label="600 rpm")
  plt.plot(x, test4y, "yo", label="800 rpm")
  plt.plot(x, test5y, "co", label="1000 rpm")
  plt.plot(x, test6y, "mo", label="1200 rpm")
  plt.plot(x, test7y, "o", label="1400 rpm", color="orange")
  plt.plot(x, test8y, "o", label="1600 rpm",color="brown")
  plt.plot(x, test9y, "o", label="1800 rpm",color="pink")
  plt.plot(x, test10y, "o", label="2000 rpm",color="GreenYellow")

  plt.plot(xp, np.polyval(test1, xp), "b-")
  plt.plot(xp, np.polyval(test2, xp), "g-")
  plt.plot(xp, np.polyval(test3, xp), "r-")
  plt.plot(xp, np.polyval(test4, xp), "y-")
  plt.plot(xp, np.polyval(test5, xp), "c-")
  plt.plot(xp, np.polyval(test6, xp), "m-")
  plt.plot(xp, np.polyval(test7, xp), "-", color="orange")
  plt.plot(xp, np.polyval(test8, xp), "-", color="brown")
  plt.plot(xp, np.polyval(test9, xp), "-", color="pink")
  plt.plot(xp, np.polyval(test10, xp), "-",color="GreenYellow")


  plt.title("Thrust vs. Blade Number", fontsize=15)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([3,4,5,6])
  plt.yticks([0,1,2,3,4,5,6,7,8,9,10]) 

  plt.legend(loc="upper left", prop={'size': 4.5})

  plt.savefig("thrustvsblade.png")
  plt.show()