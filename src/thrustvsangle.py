from api import *
import matplotlib.pyplot as plt
import numpy as np

def plot_thrustvsangle_graphs():

  x = np.array([30, 32.5, 35, 37.5, 40, 42.5, 45])

  test1y = np.array([0.07259,0.0819,0.093,0.061,0.078,0.070,0.069])
  test2y = np.array([0.300,0.326,0.371,0.246,0.316,0.284,0.284])
  test3y = np.array([0.679,0.687,0.834,0.559,0.720,0.651,0.642])
  test4y = np.array([1.216,1.212,1.477,0.929,1.273,1.155,1.154])
  test5y = np.array([1.963,1.895,2.32,1.549,2.005,1.801,1.794])
  test6y = np.array([2.718,2.989,3.336,2.180,2.985,2.668,2.691])
  test7y = np.array([3.778,3.740,4.550,2.991,3.915,3.428,3.463])
  test8y = np.array([4.840,5.235,5.935,3.904,5.093,4.574,4.592])
  test9y = np.array([6.136,6.641,7.553,4.713,6.461,5.81,5.722])
  test10y = np.array([7.864,7.598,9.320,7.514,8.044,7.218,7.335])


  test1 = np.polyfit(x, test1y, 6)
  test2 = np.polyfit(x, test2y, 6)
  test3 = np.polyfit(x, test3y, 6)
  test4 = np.polyfit(x, test4y, 6)
  test5 = np.polyfit(x, test5y, 6)
  test6 = np.polyfit(x, test6y, 6)
  test7 = np.polyfit(x, test7y, 6)
  test8 = np.polyfit(x, test8y, 6)
  test9 = np.polyfit(x, test9y, 6)
  test10 = np.polyfit(x, test10y, 6)
  
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


  plt.title("Thrust vs. Angle", fontsize=16)
  plt.ylabel("Thrust", fontsize=12)
  plt.xlabel("RPM", fontsize=12)

  plt.grid(b=None, which='major', axis='both')

  plt.xticks([30, 32.5, 35, 37.5, 40, 42.5, 45])
  plt.yticks([0,1,2,3,4,5,6,7,8,9]) 

  plt.legend(loc="upper right", prop={'size': 4})

  plt.savefig("thrustvsangle.png")
  plt.show()